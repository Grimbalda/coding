import csv
import datetime
from collections import defaultdict


class HotelAvailabilityCalculator(object):
    def __init__(self, hotels_file, bookings_file):
        self.bookings = self.import_bookings(bookings_file)
        self.hotel_capacity = self.import_hotels(hotels_file)

    def import_bookings(self, filename):
        data = self._import_from_file(filename)
        bookings = defaultdict(list)
        for booking in data:
            bookings[booking[0]].append((datetime.datetime.strptime(booking[1].replace(' ', ''), '%Y-%m-%d'),
                                         datetime.datetime.strptime(booking[2].replace(' ', ''), '%Y-%m-%d')))
        return bookings

    def import_hotels(self, filename):
        hotels = {data[0]: int(data[1]) for data in self._import_from_file(filename)}
        return hotels

    def check_availability(self, check_in, check_out):
        available = []
        dates = list(self._generate_date_range(check_in, check_out))
        for hotel in self.hotel_capacity.keys():
            if self._is_hotel_free_for_booking_on_dates(hotel, dates):
                available.append(hotel)
        return available

    @staticmethod
    def _import_from_file(filename):
        data = []
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, lineterminator='\r\n')
            for line in csvreader:
                if not line[0].startswith('#'):
                    data.append(line)
        return data

    @staticmethod
    def _generate_date_range(start_date, end_date):
        date = start_date
        while date <= end_date:
            yield date
            date = date + datetime.timedelta(days=1)

    def _is_hotel_free_for_booking_on_dates(self, hotel, period):
        if self.hotel_capacity[hotel] <= 0:
            return False
        for date in period:
            if not self._is_hotel_free_for_booking_on_date(hotel, date):
                return False
        return True

    def _is_hotel_free_for_booking_on_date(self, hotel, date):
        bookings_containing_date = 0
        for booking in self.bookings[hotel]:
            if booking[0] <= date <= booking[1]:
                bookings_containing_date += 1
            if bookings_containing_date >= self.hotel_capacity[hotel]:
                return False
        return True
