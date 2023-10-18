import datetime
import sys


class DateUtil:
    def __init__(self):
        pass

    def set_date_format(self,date_to_convert,new_date_format='%d-%m-%Y'):
        """_summary_

        Args:
            date_to_convert (datetime): Date to convert in new_date_format
            new_date_format (str, optional): New date format used to convert date. Defaults to '%d-%m-%Y'.

        Returns:
            String: Date in new format specified
        """
        try:
            date_to_convert = date_to_convert.strftime(new_date_format)
            return date_to_convert
        except TypeError:
            print('Date to convert has not valid type!')
            sys.exit(-1)
        except AttributeError:
            print('Date to convert has not valid type! String has not attribute strftime!')
            sys.exit(-1)

