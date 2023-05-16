class TimeToWordConvertingInterface:
    def convert(self, hours: int, minutes: int) -> str:  # type: ignore
        pass


class TimeToWordConverter:
    hour_words = {
        1: 'од',
        2: 'дв',
        3: 'тр',
        4: 'четыре',
        5: 'пят',
        6: 'шест',
        7: 'сем',
        8: 'вос',
        9: 'девят',
        10: 'десят',
        11: 'одиннадцат',
        12: 'двенадцат'
    }
    minute_words = {
        1: 'одна минута',
        2: 'две минуты',
        3: 'три минуты',
        4: 'четыре минуты',
        5: 'пять минут',
        6: 'шесть минут',
        7: 'семь минут',
        8: 'восемь минут',
        9: 'девять минут',
        10: 'десять минут',
        11: 'одиннадцать минут',
        12: 'двенадцать минут',
        13: 'тринадцать минут',
        14: 'четырнадцать минут',
        15: 'четверть',
        16: 'шестнадцать минут',
        17: 'семнадцать минут',
        18: 'восемнадцать минут',
        19: 'девятнадцать минут',
        20: 'двадцать минут',
        21: 'двадцать одна минута',
        22: 'двадцать две минуты',
        23: 'двадцать три минуты',
        24: 'двадцать четыре минуты',
        25: 'двадцать пять минут',
        26: 'двадцать шесть минут',
        27: 'двадцать семь минут',
        28: 'двадцать восемь минут',
        29: 'двадцать девять минут',
        30: 'половина',
    }

    @staticmethod
    def convert(hours, minutes):
        hour = TimeToWordConverter.hour_words[hours]
        minute = TimeToWordConverter.minute_words[minutes]

        if minutes == 0:
            if hours == 1:
                return hour + "ин час"
            if hours == 2:
                return hour + "а часа"
            if hours == 3:
                return hour + "и часа"
            if hours == 4:
                return hour + "часа"
            if hours in [5, 6, 7, 9, 10, 11, 12]:
                return hour + "ь часов"
            if hours == 8:
                return hour + "емь часов"

        if minutes == 1 and 5 <= hours <= 12 and hours != 8:

            return minute + " после " + hour + "и"
        if minutes == 1 and hours == 8:
            return minute + " после " + hour + "ьми"

        if minutes >= 1 and minutes < 30 and minutes != 15 and hours < 5:
            if hours == 1:
                return minute + " после часа"
            elif hours == 2:
                return minute + " после двух"
            elif hours == 3:
                return minute + " после трех"
            elif hours == 4:
                return minute + " после четырех"
            elif hours == 5:
                return minute + " после пяти"

        if minutes == 15:
            if hours == 1:
                return minute + " второго"
            elif hours == 2:
                return minute + " третьего"
            elif hours == 3:
                return minute + " четвертого"
            elif hours == 4:
                return minute + " пятого"
            elif hours == 5:
                return minute + " шестого"
            elif hours == 6:
                return minute + " седьмого"
            elif hours == 7:
                return minute + " восьмого"
            elif hours == 8:
                return minute + " девятого"
            elif hours == 9:
                return minute + " десятого"
            elif hours == 10:
                return minute + " одиннадцатого"
            elif hours == 11:
                return minute + " двенадцатого"
            elif hours == 12:
                return minute + " первого"

        if minutes == 59:
            if hours == 0:
                return TimeToWordConverter.minute_words[
                           60 - minutes] + " до часа"
            elif hours == 1:
                return TimeToWordConverter.minute_words[
                           60 - minutes] + " минута после часа"
            elif hours == 2:
                return TimeToWordConverter.minute_words[60 - minutes] + " до трех"
            elif hours == 3:
                return TimeToWordConverter.minute_words[60 - minutes] + " до четырех"
            elif hours == 4:
                return TimeToWordConverter.minute_words[60 - minutes] + " до пяти"
            elif hours == 5:
                return TimeToWordConverter.minute_words[60 - minutes] + " до шести"
            elif hours == 6:
                return TimeToWordConverter.minute_words[60 - minutes] + " до семи"
            elif hours == 7:
                return TimeToWordConverter.minute_words[60 - minutes] + " до восьми"
            elif hours == 8:
                return TimeToWordConverter.minute_words[60 - minutes] + " до девяти"
            elif hours == 9:
                return TimeToWordConverter.minute_words[60 - minutes] + " до десяти"
            elif hours == 10:
                return TimeToWordConverter.minute_words[60 - minutes] + " до одиннадцати"
            elif hours == 11:
                return TimeToWordConverter.minute_words[60 - minutes] + " до двенадцати"
            elif hours == 12:
                return TimeToWordConverter.minute_words[60 - minutes] + " до часа"

            if minutes < 30 and hours >= 5 and hours <= 12 and hours != 8:
                return minute + " после " + hour + "и"
            if minutes < 30 and hours == 8:
                return minute + " после " + hour + "ьми"

        if minutes == 30:
            if hours == 1:
                return minute + " второго"
            elif hours == 2:
                return minute + " третьего"
            elif hours == 3:
                return minute + " четвертого"
            elif hours == 4:
                return minute + " пятого"
            elif hours == 5:
                return minute + " шестого"
            elif hours == 6:
                return minute + " седьмого"
            elif hours == 7:
                return minute + " восьмого"
            elif hours == 8:
                return minute + " девятого"
            elif hours == 9:
                return minute + " десятого"
            elif hours == 10:
                return minute + " одиннадцатого"
            elif hours == 11:
                return minute + " двенадцатого"
            elif hours == 12:
                return minute + " первого"

        if minutes == 45:
            if hours == 1:
                return "пятнадцать минут до двух"
            elif hours == 2:
                return "пятнадцать минут до трех"
            elif hours == 3:
                return "пятнадцать минут до четырех"
            elif hours == 4:
                return "пятнадцать минут до пяти"
            elif hours == 5:
                return "пятнадцать минут до шести"
            elif hours == 6:
                return "пятнадцать минут до семи"
            elif hours == 7:
                return "пятнадцать минут до восьми"
            elif hours == 8:
                return "пятнадцать минут до девяти"
            elif hours == 9:
                return "пятнадцать минут до десяти"
            elif hours == 10:
                return "пятнадцать минут до одиннадцати"
            elif hours == 11:
                return "пятнадцать минут до двенадцати"
            elif hours == 12:
                return "пятнадцать минут до часа"

            if minutes > 30 and (hours % 12) + 1 >= 5 and (
                    hours % 12) + 1 <= 12 and (hours % 12) + 1 != 8:
                return TimeToWordConverter.minute_words[60 - minutes] + " до " + TimeToWordConverter.hour_words[
                    (hours % 12) + 1] + "и"
            if minutes > 30 and (hours % 12) + 1 < 5:
                if hours == 1:
                    return TimeToWordConverter.minute_words[60 - minutes] + " до двух"
                elif hours == 2:
                    return TimeToWordConverter.minute_words[60 - minutes] + " до трех"
                elif hours == 3:
                    return TimeToWordConverter.minute_words[60 - minutes] + " до четырех"
                elif hours == 4:
                    return TimeToWordConverter.minute_words[60 - minutes] + " до пяти"
            if minutes > 30 and (hours % 12) + 1 == 8:
                return TimeToWordConverter.minute_words[60 - minutes] + " до " + TimeToWordConverter.hour_words[(hours % 12) + 1] + "ьми"
            minute = TimeToWordConverter.minute_words[60 - minutes]
            return minute + " до часа"

    def test_time_to_word_converter(self) -> None:
        hours = int(input())
        minutes = int(input())

        converter = TimeToWordConverter()
        result = converter.convert(hours, minutes)

        print(result)


converter = TimeToWordConverter()
converter.test_time_to_word_converter()
