from datetime import timedelta

from django.utils import timezone

from celery import shared_task

from myhabits.models import Habit
from myhabits.services import send_telegram_message


@shared_task
def send_habit():
    """Метод отправляет сообщение о начале выполнения привычки в установленное время """
    current_time = timezone.now()
    start = current_time.replace(second=0, microsecond=0)
    end = start + timedelta(minutes=1)
    habits = Habit.objects.filter(owner__isnull=False, date_time__gte=start, date_time__lt=end, )
    for habit in habits:
        if habit.owner.tg_chat_id:
            try:
                message = f"Пора {habit.habit.lower()}!"
                send_telegram_message(habit.owner.tg_chat_id, message)
            except Exception as e:
                print(f'Ошибка отправки сообщения: {e}')
