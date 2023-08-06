import numpy as np
import math


class Missing_Treatment():
    '''
        Treat missing data in an existing metric
    '''
    def __init__(self, arr):
        '''
            Arg:
                arr (array): Input time series data (reverse chronological) {'timestamp': <date str in %Y-%m-%dT%H:%M:%S.%fZ>, 'value': None}.
                    Missing data should be represented as 'timestamp': <date str in %Y-%m-%dT%H:%M:%S.%fZ>, 'value': None}
        '''
        self.arr = arr

    @staticmethod
    def __interpolate(left, right):
        return 0.5 * (left + right)

    def missing_treatment(self):
        '''
            #Private
            fill out missing data with nearest neighbor interpolation
            Returns:
                treated_arr: each missing value has been appropriately filled with nearest neighbor interpolation
        '''
        treated_arr = self.arr
        # filling the missing value at the beginning of the array
        if math.isnan(treated_arr[0]) and not math.isnan(treated_arr[1]):
            '''
                filling the missing value at the beginning of the array
                example: np.array([float('nan'), 11, 12, 14, 15, 15, 16, 17, 18, 21, 27, 29, 31, 33, 34, 37])
            '''
            treated_arr[0] = Missing_Treatment.__interpolate(treated_arr[1], treated_arr[1])

        i = 0
        while i < (treated_arr.size - 1):
            if math.isnan(treated_arr[i]) and not math.isnan(treated_arr[i+1]):
                '''
                    filling the missing treated_arr right in between two non-missing treated_arrs
                    example: np.array([7, 8, float('nan'), 11, 12, 14, 15, 15, 16, 17, 18, 21, 27, 29, 31, 33, 34, 37])
                '''
                treated_arr[i] = Missing_Treatment.__interpolate(treated_arr[i-1], treated_arr[i+1])
            if math.isnan(treated_arr[i]) and math.isnan(treated_arr[i+1]):
                '''
                    treating two consecutive missing treated_arrs
                    example: np.array([7, 8, float('nan'), float('nan'), 12, 14, 15, 15, 16, 17, 18, 21, 27, 29, 31, 33, 34, 37])
                '''
                j = i+2
                while True:
                # filling the missing treated_arr for the last but one element
                    if j == treated_arr.size:
                        '''
                            treating two consecutive missing treated_arrs at the end
                            example: np.array([7, 8, float('nan'), float('nan'), 12, 14, 15, 15, 16, 17, 18, 21, 27, float('nan'), float('nan')])
                        '''
                        for k in range(i, j - 1):
                            treated_arr[k] = Missing_Treatment.__interpolate(treated_arr[k - 1], treated_arr[k - 1])
                        break
                    elif not math.isnan(treated_arr[j]):
                        '''
                            filling out two inner missing treated_arrs
                            example: np.array([9, 10, 12, 14, 15, 15, 16, 17, 18, 21, 27, float('nan'), float('nan'), 29, 30, 34, 45])
                        '''
                        for k in range(i, j):
                            left_index = j if k == 0 else k - 1
                            treated_arr[k] = Missing_Treatment.__interpolate(treated_arr[left_index], treated_arr[j])
                        break
                    else:
                        j += 1
            i += 1
        if math.isnan(treated_arr[-1]) and not math.isnan(treated_arr[-2]):
            treated_arr[-1] = Missing_Treatment.__interpolate(treated_arr[-2], treated_arr[-2])

        return treated_arr
    
SCALE_FACTOR = 1.4826
SCALE_FACTOR_LOG = np.log(1.4826)

class NotEnoughData(Exception):
    def __init__(self, message):
        self.message = message

class Model():
    '''
        Compute the model parameters for the input time series data
    '''

    def __init__(self, data, crit=None, perc=None, window=60, is_log=True):
        '''
            Arg:
                data (array): Input time series data (reverse chronological) {'timestamp_ms': <unix time>, 'value': None}.
                    Missing data should be represented as 'timestamp_ms': <unix time>, 'value': NaN}
                
            Keyword Arg:
                window (int): Size of input data (default=60)
                crit (float):  A factor that determines how many multiples of scales are to considered for normalcy detection (default=2.5)
                is_log (boolean): A flag which defines if the log transformation to implemented (default=True)
        '''

        if len(data) < window:
            raise ValueError('data length cannot be lower than ' + str(window))

        data = data[0:window]
        value = np.array([])
        value = np.full(len(data), math.nan)
        num_missing = 0
        prev_timestamp = 0
        for i, datapoint in enumerate(data):
            datapoint_value = datapoint.value
            if not math.isnan(datapoint_value):
                if datapoint_value + 1 <= 0:
                    raise ValueError('each element in the input list must be greater than -1')
                value[i] = np.log(datapoint_value + 1) if is_log else datapoint_value
            else:
                value[i] = math.nan
                num_missing += 1
                # if more than 20% of the window is missing then we quit computation
                if num_missing > 0.2 * window:
                    raise NotEnoughData('too much missing data')

            curr_timestamp = datapoint.timestamp_ms
            if i and (curr_timestamp - prev_timestamp) >= 0:
                raise ValueError('the time must be strictly decreasing for reverse-chrono representation.')
            prev_timestamp = curr_timestamp

        # check if any of the columns are empty
        if not value.size:
            raise ValueError('data cannot be empty')

        self.value = Missing_Treatment(value).missing_treatment() if num_missing else value
        self.median = np.nanmedian(self.value)
        if is_log:
            self.allowance = 0.1
        else:
            margin = 0.01
            self.allowance = round(max(self.median * margin, 0.5), 2)
        self.crit = 2.5 if crit is None else crit
        self.is_log = is_log
        self.perc = 75 if perc is None else perc

    def __scale_factor(self):
        return SCALE_FACTOR if not self.is_log else SCALE_FACTOR_LOG

    def model(self):
        '''
            #Public
            fit time series data
            Returns:
                model_params (object): it includes the properties of the distribution (such as estimate, scale) and allowance
                self.is_log (boolean): a flag that indicates whether the log transformation has been performed
                self.crit (scalar, float): A factor that determines how many multiples of scales are to considered \
                    for normalcy detection (default=2.5)
        '''
        estimate = self.median

        scale = np.nanpercentile(np.abs(self.value - estimate), self.perc) * self.__scale_factor()
        estimate = round(estimate, 2)
        scale = round(scale, 2)
        allowance = round(self.allowance, 2)
        model_params = {'estimate': estimate, 'scale': scale, 'allowance': allowance}

        return model_params, self.is_log, self.crit, self.perc

class Baseline():
    '''
        Compute baseline for a time series data
    '''

    def __init__(self, data, crit, perc, false_positive_threshold=None, is_low=True):
        '''
            Arg:
                data (array): time series data (reverse chronological)
            Keyword Arg:
                crit (float): critical multiplier value (default=None)
                perc (float): critical baselining percentage (default=None)
                false_positive_threshold (boolean): whether to use any false_positive_threshold (default=None)
                is_low (boolean): whether anomalies for the lower thresholds are to be detected (default=False)
        '''
        self.is_low = is_low
        self.false_positive_threshold = false_positive_threshold
        self.model = Model(data, crit, perc)
    
    def baseline(self):
        '''
            # Public
            Computing upper and lower thresholds
            Returns:
                an object: upper and lower threshold values and is_low
        '''
        model_params, is_log, crit, _ = self.model.model()
        estimate = model_params['estimate']
        scale = model_params['scale']
        allowance = model_params['allowance']
        lower_threshold = estimate - crit * scale - allowance
        upper_threshold = estimate + crit * scale + allowance
        
        if is_log:
            output = {
                'upper_threshold': np.exp(upper_threshold)-1 if not self.false_positive_threshold else \
                    max(np.exp(upper_threshold)-1, self.false_positive_threshold),
                'lower_threshold': np.exp(lower_threshold)-1,
                'is_low': bool(self.is_low),
                'estimate': np.exp(estimate) - 1,
                'scale': np.exp(scale) - 1
            }
        else:
            output = {
                'upper_threshold': upper_threshold if not self.false_positive_threshold else \
                    max(upper_threshold, self.false_positive_threshold),
                'lower_threshold': lower_threshold,
                'is_low': bool(self.is_low),
                'estimate': estimate,
                'scale': scale
            }
        # TODO: Reducing the lower_threshold by 0.5% to reduce false positives.
        output['lower_threshold'] -= 0.005 * (output['upper_threshold'] - output['lower_threshold'])

        return output
    

    
