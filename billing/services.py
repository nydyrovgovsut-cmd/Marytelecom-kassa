from django.db import transaction
from .models import Subscriber, Transaction, TransactionStatus

class BillingService:
    @staticmethod
    def process_payment(phone_number: str, amount: float, operator_user=None) -> Transaction:
        """
        Проведение платежа и автоматическое пополнение баланса абонента
        """
        if amount <= 0:
            raise ValueError("Сумма платежа должна быть больше нуля")

        with transaction.atomic():
            # Блокируем запись абонента для предотвращения Race Condition
            subscriber = Subscriber.objects.select_for_update().get(phone_number=phone_number)
            
            # 1. Создаем транзакцию
            txn = Transaction.objects.create(
                subscriber=subscriber,
                amount=amount,
                status=TransactionStatus.PENDING,
                created_by=operator_user
            )

            # 2. Пополняем баланс
            subscriber.balance += amount
            subscriber.save()

            # 3. Фиксируем успешный статус
            txn.status = TransactionStatus.SUCCESS
            txn.save()

            return txn