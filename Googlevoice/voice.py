from gtts import gTTS
import os
import tkinter, tkinter.filedialog

yn={'y':True, 'yes':True, 'n':False, 'no':False}
lang={'j':'ja', 'ja':'ja', 'jp':'ja', 'jn':'ja','japanese':'ja', 'japan':'ja', 'e':'en', 'en':'en', 'eng':'en', 'english':'en'}

while True:
    try:

        inp = yn[input('Loading files? y/N : ').lower()]

        print(inp)

        if inp == True:

            root = tkinter.Tk()

            root.withdraw()

            fTyp = [("","*")]
            iDir = os.path.abspath(os.path.dirname(__file__))
            file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

            print(file)

            while True:
                try:

                    lan = lang[input('Language? ja/en : ').lower()]

                    f = open(file, 'r', encoding = "utf-8")
                    data1 = f.read()

                    f.close()

                    tts = gTTS(text = data1, lang = lan)
                    filename = input('mp3 file name? => ')
                    tts.save(filename + '.mp3')
                    print('Completed!')
                    os.system('PAUSE')

                    break

                except:
                    pass

                print('Error! Input again.')

        elif inp == False:

            file = input('Enter the words you want to output as mp3. => ')

            while True:
                try:

                    lan = lang[input('Language? ja/en : ').lower()]

                    tts = gTTS(text = file, lang = lan)
                    filename = input('mp3 file name? => ')

                    tts.save(filename + '.mp3')
                    print('Completed!')
                    os.system('PAUSE')

                    break

                except:
                    pass

                print('Error! Input again.')

        break

    except:
        pass

    print('Error! Input again.')
