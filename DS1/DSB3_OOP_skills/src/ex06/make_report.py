from analytics import Research
from config import (
    NUM_OF_STEPS,
    REPORT_TEMPLATE,
    TELEGRAM_URL
)


def main():
    research = Research('data.csv')

    try:
        data = research.file_reader()

        analytics = Research.Analytics(data)

        heads, tails = analytics.counts()

        head_percent, tail_percent = analytics.fractions(
            heads,
            tails
        )

        prediction = analytics.predict_random(
            NUM_OF_STEPS
        )

        pred_heads = 0
        pred_tails = 0

        for item in prediction:
            if item == [1, 0]:
                pred_heads += 1
            else:
                pred_tails += 1

        report = REPORT_TEMPLATE.format(
            total=len(data),
            tails=tails,
            heads=heads,
            tail_percent=tail_percent,
            head_percent=head_percent,
            steps=NUM_OF_STEPS,
            pred_tails=pred_tails,
            pred_heads=pred_heads
        )

        analytics.save_file(
            report,
            'report',
            'txt'
        )

        research.send_telegram_message(
            TELEGRAM_URL,
            'The report has been successfully created'
        )

        print(report)

    except Exception:
        research.send_telegram_message(
            TELEGRAM_URL,
            "The report hasn't been created due to an error."
        )
        raise


if __name__ == '__main__':
    main()
