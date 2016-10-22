import sys
import datetime

from calculator import HotelAvailabilityCalculator


def _extract_dates(date_input):
    check_in, check_out = user_input.split(' ')
    check_in = datetime.datetime.strptime(check_in, '%Y-%m-%d')
    check_out = datetime.datetime.strptime(check_out, '%Y-%m-%d')
    return check_in, check_out


if __name__ == '__main__':
    calculator = HotelAvailabilityCalculator(sys.argv[1], sys.argv[2])
    prompt = '\nPlease specify check-in and check-out dates or enter \'q\'/\'Q\' to exit: '
    user_input = raw_input(prompt)
    while user_input not in ['q', 'Q']:
        check_in, check_out = _extract_dates(user_input)
        if check_out < check_in:
            print 'Check-out date is defined to a date prior to check-in date. Please enter new dates.'
        else:
            print '\n\n-------------------------------------'
            print 'Availability for %s - %s:' % (check_in.date(), check_out.date())
            availability = calculator.check_availability(check_in, check_out)
            if availability:
                for hotel in availability:
                    print hotel
            else:
                print 'No free rooms for specified period'
            print '-------------------------------------\n\n'
        user_input = raw_input(prompt)
