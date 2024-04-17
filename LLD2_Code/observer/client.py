from concrete_classes import BitcoinTracker, EmailNotifier


def main():
    # Observable Instance
    bitcoin_tracker = BitcoinTracker()
    # Observer Instance
    email_notifier = EmailNotifier(bitcoin_tracker)

    # Add observer to the observable
    bitcoin_tracker.add_observer(email_notifier)

    # Change the state of the observable -> This will trigger a Email notification to the observers
    bitcoin_tracker.set_price(10000)


if __name__ == "__main__":
    main()
