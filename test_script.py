from voice_assistant import voice_assistant
import datetime as dt
import random as rnd


phrases_to_answer_on_hello = [
    '',
    'DEFAULT',
    'Да',
    'Нет',
    'Занят',
    'Еще раз'
]

phrases_to_answer_on_main = [
    '',
    'DEFAULT',
    'Нет',
    'Возможно',
    'Да',
    'Еще раз',
    'Не знаю',
    'Занят',
    'Вопрос'
]

phrases_to_answer_on_hello_null = [
    '',
    'Да',
    'Нет',
    'Занят',
    'Еще раз'
]


def client_rating(nn):
    answer_on_main = rnd.randint(0, 10)
    print(f'\nClient: {answer_on_main}')
    nn.get_client_rating(answer_on_main)


def get_answer(phrases):
    return rnd.choice(phrases)


def main_logic(
    nn,
    answer_on_hello
):
    if (answer_on_hello == 'Нет' or answer_on_hello == 'Занят'):
        print('\nAssistant ended the call')
    else:
        answer_on_main = get_answer(
            phrases_to_answer_on_main
        )
        print(f'\nClient: {answer_on_main}')
        if (answer_on_main == 'Нет' or
                answer_on_main == 'Занят'):
            nn.hangup_wrong_time()

        if (answer_on_main == ''):
            nn.recommend_null()
            answer_on_main = get_answer(
                phrases_to_answer_on_main
            )
            print(f'\nClient: {answer_on_main}')

            if (answer_on_main == ''):
                nn.hangup_null()
            else:
                nn.get_client_answer_on_main(
                    answer_on_main
                )
                client_rating(nn)
        elif (answer_on_main == 'DEFAULT'):
            nn.recommend_default()
            answer_on_main = get_answer(
                phrases_to_answer_on_main
            )
            print(f'\nClient: {answer_on_main}')

            if (answer_on_main == 'DEFAULT'):
                nn.hangup_null()
            else:
                nn.get_client_answer_on_main(
                    answer_on_main
                )
                client_rating(nn)
        else:
            nn.get_client_answer_on_main(
                answer_on_main
            )
            if (answer_on_main == 'Да' or
                answer_on_main == 'Нет ' or
                    answer_on_main == 'Возможно'):
                client_rating(nn)
            else:
                answer_on_main = get_answer(
                    phrases_to_answer_on_main
                )
                print(f'\nClient: {answer_on_main}')
                nn.get_client_answer_on_main(
                    answer_on_main
                )
                client_rating(nn)


def main():
    # In my case I will use random to get client answer
    nn = voice_assistant(
        'Example_company',
    )

    nn.call(
        '+7-999-999-99-99',
        str(dt.datetime.now()).split(".")[0],
    )

    nn.hello('Андрей')

    answer_on_hello = get_answer(
        phrases_to_answer_on_hello
    )
    if (answer_on_hello == ''):
        print(f'\nClient: {answer_on_hello}')
        nn.get_client_answer_on_hello_null(
            answer_on_hello
        )
        answer_on_hello = get_answer(
            phrases_to_answer_on_hello_null
        )
        print(f'\nClient: {answer_on_hello}')

        if (answer_on_hello == ''):
            nn.hangup_null()
            print('\nAssistant ended the call')
        else:
            nn.get_client_answer_on_hello_null(
                answer_on_hello
            )
            main_logic(
                nn,
                answer_on_hello
            )
    else:
        print(f'\nClient: {answer_on_hello}')
        nn.get_clien_answer_on_hello(
            answer_on_hello
        )
        main_logic(
            nn,
            answer_on_hello
        )
