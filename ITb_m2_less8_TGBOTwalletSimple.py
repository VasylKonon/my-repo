import logging
import pickle
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler


TOKEN_BOT = "6199819510:AAH55QfOvX85r0YJZnGonK_k3dwzmr2q3lo"
user_data_income = dict()
user_data_expense = dict()
categories_expense = ["food", "car"]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(message)s',
    level=logging.INFO
)


class Operation:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount
        self.inc_or_exp = False
        self.date = datetime.now()

    def __str__(self):
        completed = "➕" if self.inc_or_exp else "➖"
        return f"{completed} {self.category} {self.amount}"


def save_data():
    with open("test.pkl", "wb") as file:
        pickle.dump((user_data_income, user_data_expense), file)


def load_data():
    try:
        with open("test.pkl", "rb") as file:
            data = pickle.load(file)
            global user_data_income, user_data_expense
            user_data_income, user_data_expense = data
    except (FileNotFoundError, EOFError):
        user_data_income = dict()
        user_data_expense = dict()


async def start(update: Update, context: CallbackContext) -> None:
    logging.info("Command /start was triggered.")
    await update.message.reply_text(
        "Welcome to my Test Bot!\n"
        "Your categories: food, car.\n"
        "Commands:\n"
        "Add income: /add <category> <amount>\n"
        "Add expense: /sub <category> <amount>\n"
        "Categories: /help\n"
        "List expenses for period: /exp <total> or <month> or <week>\n"
        "List incomes for period: /inc <total> or <month> or <week>\n"
        "Remove expense: /remove_exp <number>\n"
        "Remove income: /remove_inc <number>\n"
        "Income statistic by category for period: /inc_stat <day> or <week> or <month>\n"
        "Income expense by category for period: /exp_stat <day> or <week> or <month>\n"
    )


async def add_income(update: Update, context: CallbackContext) -> None:
    logging.info("Command /add was triggered.")
    user_id = update.message.from_user.id
    operation_parts = " ".join(context.args).split()
    operation_category = operation_parts[0].strip()
    amount = operation_parts[1].strip()

    if len(operation_parts) != 2:
        logging.info("Invalid input.")
        await update.message.reply_text("Invalid input. Need <category> <amount>")
        return

    if not user_data_income.get(user_id):
        user_data_income[user_id] = []

    operation = Operation(operation_category, int(amount))
    operation.inc_or_exp = True
    user_data_income[user_id].append(operation)
    await update.message.reply_text(f"{operation} was successfully added!")
    save_data()


async def add_expense(update: Update, context: CallbackContext) -> None:
    logging.info("Command /sub was triggered.")
    user_id = update.message.from_user.id
    operation_parts = " ".join(context.args).split()
    operation_category = operation_parts[0].strip()
    if operation_category not in categories_expense:
        logging.info("Invalid input.")
        await update.message.reply_text("Invalid input. Need choose from food, car, income.")
        return

    amount = operation_parts[1].strip()

    if len(operation_parts) != 2:
        logging.info("Invalid input.")
        await update.message.reply_text("Invalid input. Need <category> <amount>")
        return

    if not user_data_expense.get(user_id):
        user_data_expense[user_id] = []

    operation = Operation(operation_category, int(amount))
    user_data_expense[user_id].append(operation)
    await update.message.reply_text(f"{operation} was successfully added!")
    save_data()


async def for_help(update: Update, context: CallbackContext) -> None:
    logging.info("Command /help was triggered.")
    await update.message.reply_text(
        "Your categories: food, car.\n"
        "Commands:\n"
        "Add income: /add <category> <amount>\n"
        "Add expense: /sub <category> <amount>\n"
        "Categories: /help\n"
        "List expenses for period: /exp <total> or <month> or <week>\n"
        "List incomes for period: /inc <total> or <month> or <week>\n"
        "Remove expense: /remove_exp <number>\n"
        "Remove income: /remove_inc <number>\n"
        "Income statistic by category for period: /inc_stat <day> or <week> or <month>\n"
        "Income expense by category for period: /exp_stat <day> or <week> or <month>\n"
    )


async def list_expenses(update: Update, context: CallbackContext) -> None:
    logging.info("Command /exp was triggered.")
    user_id = update.message.from_user.id
    period = " ".join(context.args)

    if not user_data_expense.get(user_id):
        await update.message.reply_text("You dont have any expenses.")
        return

    if period == "total":
        result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(user_data_expense[user_id])])
        result_total = sum(e.amount for e in user_data_expense[user_id])
        await update.message.reply_text(result)
        await update.message.reply_text(f"Total expenses: {str(result_total)}")
        return

    elif period == "month":
        now = datetime.now()
        local_list_expenses = []
        total_result = 0
        for expense in user_data_expense[user_id]:
            expense_date = expense.date
            if expense_date.month == now.month and expense_date.year == now.year:
                local_list_expenses.append(expense)
                total_result += expense.amount

        if local_list_expenses:
            result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(local_list_expenses)])
            await update.message.reply_text(result)
            await update.message.reply_text(str(total_result))
        else:
            await update.message.reply_text("You dont have any expenses for this month.")
        return

    elif period == "week":
        now = datetime.now()
        week = now.isocalendar()[1]
        local_list_expenses = []
        total_result = 0
        for expense in user_data_expense[user_id]:
            expense_date = expense.date
            expense_week = expense_date.isocalendar()[1]
            if expense_week == week and expense_date.month == now.month and expense_date.year == now.year:
                local_list_expenses.append(expense)
                total_result += expense.amount

        if local_list_expenses:
            result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(local_list_expenses)])
            await update.message.reply_text(result)
            await update.message.reply_text(str(total_result))
        else:
            await update.message.reply_text("You dont have any expenses for this month.")
        return

    else:
        logging.info("Invalid period.")
        await update.message.reply_text("You entered the wrong period.")


async def list_incomes(update: Update, context: CallbackContext) -> None:
    logging.info("Command /exp was triggered.")
    user_id = update.message.from_user.id
    period = " ".join(context.args)

    if not user_data_income.get(user_id):
        await update.message.reply_text("You dont have any incomes.")
        return

    if period == "total":
        result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(user_data_income[user_id])])
        result_total = sum(e.amount for e in user_data_income[user_id])
        await update.message.reply_text(result)
        await update.message.reply_text(f"Total incomes: {str(result_total)}")
        return

    elif period == "month":
        now = datetime.now()
        local_list_expenses = []
        total_result = 0
        for expense in user_data_expense[user_id]:
            expense_date = expense.date
            if expense_date.month == now.month and expense_date.year == now.year:
                local_list_expenses.append(expense)
                total_result += expense.amount

        if local_list_expenses:
            result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(local_list_expenses)])
            await update.message.reply_text(result)
            await update.message.reply_text(f"Total incomes: {str(total_result)}")
        else:
            await update.message.reply_text("You dont have any incomes for this month.")
        return

    elif period == "week":
        now = datetime.now()
        week = now.isocalendar()[1]
        local_list_expenses = []
        total_result = 0
        for expense in user_data_expense[user_id]:
            expense_date = expense.date
            expense_week = expense_date.isocalendar()[1]
            if expense_week == week and expense_date.month == now.month and expense_date.year == now.year:
                local_list_expenses.append(expense)
                total_result += expense.amount

        if local_list_expenses:
            result = "\n".join([f"{i + 1}. {t}" for i, t in enumerate(local_list_expenses)])
            await update.message.reply_text(result)
            await update.message.reply_text(f"Total incomes: {str(total_result)}")
        else:
            await update.message.reply_text("You dont have any incomes for this month.")
        return

    else:
        logging.info("Invalid period.")
        await update.message.reply_text("You entered the wrong period.")


async def remove_expense(update: Update, context: CallbackContext) -> None:
    logging.info("Command /remove_exp was triggered.")
    user_id = update.message.from_user.id

    if not user_data_expense.get(user_id):
        await update.message.reply_text("You dont have any expenses.")
        return

    try:
        removed_idx = int(context.args[0]) - 1
        expense = user_data_expense[user_id].pop(removed_idx)
        await update.message.reply_text(f"{expense} successfully removed.")
    except (ValueError, IndexError):
        await update.message.reply_text("You entered invalid index.")

    save_data()


async def remove_income(update: Update, context: CallbackContext) -> None:
    logging.info("Command /remove_exp was triggered.")
    user_id = update.message.from_user.id

    if not user_data_expense.get(user_id):
        await update.message.reply_text("You dont have any expenses.")
        return

    try:
        removed_idx = int(context.args[0]) - 1
        expense = user_data_income[user_id].pop(removed_idx)
        await update.message.reply_text(f"{expense} successfully removed.")
    except (ValueError, IndexError):
        await update.message.reply_text("You entered invalid index.")

    save_data()


async def statistic_income_by_category(update: Update, context: CallbackContext) -> None:
    logging.info("Command /inc_stat was triggered.")
    user_id = update.message.from_user.id
    period = " ".join(context.args)

    if not user_data_income.get(user_id):
        await update.message.reply_text("You dont have any incomes.")
        return

    statistic = dict()

    for income in user_data_income[user_id]:
        income_date = income.date
        if period == "day":
            if income_date.date() == datetime.now().date():
                statistic.setdefault(income.category, 0)
                statistic[income.category] += income.amount
        elif period == "week":
            if income_date.isocalendar()[1] == datetime.now().isocalendar()[1] \
                    and income_date.year == datetime.now().year:
                statistic.setdefault(income.category, 0)
                statistic[income.category] += income.amount
        elif period == "month":
            if income_date.month == datetime.now().month and income_date.year == datetime.now().year:
                statistic.setdefault(income.category, 0)
                statistic[income.category] += income.amount

    if statistic:
        result = "\n".join([f"{category}: {amount}" for category, amount in statistic.items()])
        result_total = sum(v for k, v in statistic.items())
        await update.message.reply_text(result)
        await update.message.reply_text(f"Total income: {str(result_total)}")


async def statistic_expense_by_category(update: Update, context: CallbackContext) -> None:
    logging.info("Command /exp_stat was triggered.")
    user_id = update.message.from_user.id
    period = " ".join(context.args)

    if not user_data_expense.get(user_id):
        await update.message.reply_text("You dont have any expenses.")
        return

    statistic = dict()

    for expense in user_data_expense[user_id]:
        expense_date = expense.date
        if period == "day":
            if expense_date.date() == datetime.now().date():
                statistic.setdefault(expense.category, 0)
                statistic[expense.category] += expense.amount
        elif period == "week":
            if expense_date.isocalendar()[1] == datetime.now().isocalendar()[1]\
                    and expense_date.year == datetime.now().year:
                statistic.setdefault(expense.category, 0)
                statistic[expense.category] += expense.amount
        elif period == "month":
            if expense_date.month == datetime.now().month and expense_date.year == datetime.now().year:
                statistic.setdefault(expense.category, 0)
                statistic[expense.category] += expense.amount

    if statistic:
        result = "\n".join([f"{category}: {amount}" for category, amount in statistic.items()])
        result_total = sum(v for k, v in statistic.items())
        await update.message.reply_text(result)
        await update.message.reply_text(f"Total expenses: {str(result_total)}")


def run():
    app = ApplicationBuilder().token(TOKEN_BOT).build()
    logging.info("Application build successfully!")

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", for_help))
    app.add_handler(CommandHandler("add", add_income))
    app.add_handler(CommandHandler("sub", add_expense))
    app.add_handler(CommandHandler("exp", list_expenses))
    app.add_handler(CommandHandler("inc", list_incomes))
    app.add_handler(CommandHandler("remove_exp", remove_expense))
    app.add_handler(CommandHandler("remove_inc", remove_income))
    app.add_handler(CommandHandler("inc_stat", statistic_income_by_category))
    app.add_handler(CommandHandler("exp_stat", statistic_expense_by_category))

    app.run_polling()


if __name__ == "__main__":
    load_data()
    run()
