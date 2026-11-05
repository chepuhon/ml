from analytics import Research
from config import NUM_OF_STEPS, REPORT_TEMPLATE


def main():
    research = Research("data.csv")

    data = research.file_reader()

    analytics = Research.Analytics(data)

    heads, tails = analytics.counts()

    head_percent, tail_percent = analytics.fractions(
        heads,
        tails
    )

    forecast = analytics.predict_random(NUM_OF_STEPS)

    pred_heads = 0
    pred_tails = 0

    for item in forecast:
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

    print(report)

    analytics.save_file(
        report,
        "report",
        "txt"
    )


if __name__ == '__main__':
    main()
