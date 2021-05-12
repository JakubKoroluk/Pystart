from datetime import datetime, timedelta


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.title = title
        self.date = date


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings

    def add(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting

    # def show_all_meetings(self):
    #     for x in self.meetings:
    #         return f'Data spotkania {self.meetings}'

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            meeting_date += timedelta(minutes=60)
        return meeting_date
        # stworzenie zmiennej potencjalnej godziny spotkania
        # while - dopoki potencjalna godzina spotkania nie jest wolna
        # dodawaj po jednej godzinie do potencjalnej godziny spotkania


def test_add_meeting():
    # given
    meeting = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    meeting2 = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    calendar = Calendar()
    # when
    calendar.add(meeting)
    calendar.add(meeting2)

    # then
    assert len(calendar.meetings) == 1


def test_check_next():
    # given
    meeting = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    meeting2 = Meeting(datetime(2020, 5, 2, 13, 0), 'Golf')
    calendar = Calendar()
    calendar.add(meeting)
    calendar.add(meeting2)

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 5, 2, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 5, 2, 14, 0)
