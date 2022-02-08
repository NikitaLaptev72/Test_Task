import datetime as dt
import assistant_phrases as phrases


class voice_assistant:
    hello_null_result = 0

    def __init__(
        self,
        company_name
    ):
        self.company = company_name

    def call(
        self,
        msisdn,
        date=str(dt.datetime.now()).split(".")[0],
        channel=None,
        script=None,
        entry_point='main',
        transport='sip'
    ):
        try:
            if (self.check_date(date) == 'now'):
                # Some logic to start call now
                print(f"\nThe number {msisdn} will be called now")
            elif (self.check_date(date) == 'later'):
                # Some logic to start call later
                print(f'The number {msisdn} will be called later')
            else:
                raise ('Something went wrong in check_date')
        except Exception as e:
            print(f"Something went wrong: {e}")

    # Function to check date validity
    def check_date(
        self,
        date
    ):
        try:
            dt.datetime.strptime(
                date,
                '%Y-%m-%d %H:%M'
                )
            return 'now'
        except:
            try:
                try:
                    dt.datetime.strptime(
                        date,
                        '%Y-%m-%d %H:%M:%S'
                    )
                    return 'now'
                except:
                    try:
                        dt.datetime.strptime(
                            date,
                            '%H:%M:%S'
                        )
                        return 'later'
                    except:
                        dt.datetime.strptime(
                            date,
                            '%H:%M'
                        )
                        return 'later'
            except Exception as e:
                print(f"Something went wrong: {e}")

    # Some logic to activate voice assistant and
    #   to get a response for the assistant
    # In my case I will use print() to replace calling assistant functions

    def hello(
        self,
        client_name
    ):
        print(phrases.hello_phrase.replace(
            'NAME', client_name
            ).replace(
                'COMPANY', self.company
            )
        )

    def get_clien_answer_on_hello(
        self,
        client_answer
    ):
        hello_result_variants = {
            'DEFAULT': 'self.recommend_main',
            'Да': 'self.recommend_main',
            'Нет': 'self.hangup_wrong_time',
            'Занят': 'self.hangup_wrong_time',
            'Еще раз': 'self.hello_repeat'
        }
        eval(hello_result_variants[client_answer])()

    def get_client_answer_on_hello_null(
        self,
        client_answer
    ):
        hello_null_result_variants = {
            '': 'self.hello_null',
            'Да': 'self.recommend_main',
            'Нет': 'self.hangup_wrong_time',
            'Занят': 'self.hangup_wrong_time',
            'Еще раз': 'self.hello_repeat'
        }
        eval(hello_null_result_variants[client_answer])()

    def get_client_answer_on_main(
        self,
        client_answer
    ):
        main_result_variants = {
            '': 'self.recommend_null',
            'DEFAULT': 'self.recommend_default',
            'Нет': 'self.recommend_score_negative',
            'Возможно': 'self.recommend_score_neutral',
            'Да': 'self.recommend_score_positive',
            'Еще раз': 'self.recommend_repeat',
            'Не знаю': 'self.recommend_repeat_2',
            'Занят': 'self.hangup_wrong_time',
            'Вопрос': 'self.forward'
        }
        eval(main_result_variants[client_answer])()

    def get_client_rating(
        self,
        rating
    ):
        if rating in range(0, 9):
            self.hangup_negative()
        elif rating in range(9, 11):
            self.hangup_positive()
        
        print('\nAssistant ended the call')
        exit()

    def hello_null(
        self
    ):
        print(phrases.hello_null_phrase)

    def recommend_main(
        self
    ):
        print(phrases.recommend_main_phrase)

    def hangup_wrong_time(
        self
    ):
        print(phrases.hangup_wrong_time_phrase)
        print('\nAssistant ended the call')
        exit()

    def hello_repeat(
        self
    ):
        print(phrases.hello_repeat_phrase.replace(
                'COMPANY', self.company
            )
        )

    def recommend_repeat(
        self
    ):
        print(phrases.recommend_repeat_phrase)

    def recommend_repeat_2(
        self
    ):
        print(phrases.recommend_repeat_2_phrase)

    def recommend_score_negative(
        self
    ):
        print(phrases.recommend_score_negative_phrase)

    def recommend_score_neutral(
        self
    ):
        print(phrases.recommend_score_neutral_phrase)

    def recommend_score_positive(
        self
    ):
        print(phrases.recommend_score_positive_phrase)

    def recommend_null(
        self
    ):
        print(phrases.recommend_null_phrase)

    def recommend_default(
        self
    ):
        print(phrases.recommend_default_phrase)

    def hangup_positive(
        self
    ):
        print(phrases.hangup_positive_phrase)
        print('\nAssistant ended the call')
        exit()

    def hangup_negative(
        self
    ):
        print(phrases.hangup_negative_phrase)
        print('\nAssistant ended the call')
        exit()

    def hangup_null(
        self
    ):
        print(phrases.hangup_null__phrase)
        print('\nAssistant ended the call')
        exit()

    def forward(
        self
    ):
        print(phrases.forward_phrase)
        print('\nAssistant ended the call')
        exit()
