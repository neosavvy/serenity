import fire

from serenity.equity.sharadar_api import init_quandl, create_sharadar_session


def load_sharadar_events():
    init_quandl()
    session = create_sharadar_session()
    session.commit()


if __name__ == '__main__':
    fire.Fire(load_sharadar_events)
