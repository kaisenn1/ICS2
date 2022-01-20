import asyncio
def something_async():
    print('something_async start')
    print('something_async done')


def x():
    for count in range(5):
        something_async()
    print('done')

x()