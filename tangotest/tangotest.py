# coding: utf-8

import re
import random
import os
import sys
import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

name = '英単語問題自動作成ツール'

root = Tk()
root.geometry('500x200')
root.title(name)
root.resizable(False, False)

def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

def run():

	source = file1.get()

	with open(source) as f:
		data = f.read()

	english_words = re.findall('[a-z,A-Z]+', data)
	japanese_words = re.findall('[ぁ-ん,ァ-ン,\u4E00-\u9FF0,ー,～,/,]+', data)

	words_list = dict(zip(english_words, japanese_words))

	test_count = 5 #問題集の数
	quest_count = 30 #問題の数
	wrong_count = 4 #間違いの答えの数

	en = english_words
	ja = japanese_words

	main_words = en #問題
	sub_words = ja #回答
	asking = wrong_count + 1

	for test_num in range(test_count):
		with open('英単語テスト({:02d}).txt'.format(test_num + 1), 'w') as f:

			f.write('英単語テスト({})\n\n'.format(test_num + 1))

			for question_num in range(quest_count):
			    question_word = random.choice(main_words)
			    correct_answer = words_list[question_word]

			    sub_words_copy = sub_words.copy()
			    sub_words_copy.remove(correct_answer)
			    wrong_answers = random.sample(sub_words_copy, wrong_count)

			    answer_options = [correct_answer] + wrong_answers

			    random.shuffle(answer_options)

			    f.write('問{}, {}\n\n'.format(question_num + 1, question_word))

			    for i in range(asking):
			        f.write('{}. {}\n'.format(i + 1, answer_options[i]))
			    f.write('\n\n')

	messagebox.showinfo(name, u'英単語テストファイルの作成が完了しました。')

frame1 = ttk.Frame(root, padding=10)
frame1.grid()
frame1.place(x=0, y=0)

# 参照ボタンの作成
button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
button1.grid(row=0, column=3)
button1.place(x=371, y=8)

# ラベルの作成
# 「ファイル」ラベルの作成
s = StringVar()
s.set('ファイル>>')
label1 = ttk.Label(frame1, textvariable=s)
label1.grid(row=0, column=0)

# 参照ファイルパス表示ラベルの作成
file1 = StringVar()
file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
file1_entry.grid(row=0, column=2)

# Frame2の作成
frame2 = ttk.Frame(root, padding=(0,5))
frame2.grid(row=1)

# Startボタンの作成
button2 = ttk.Button(root, text='Start', command=run)
button2.grid(row=0, column=2)
button2.place(x=325, y=175)

# Cancelボタンの作成
button3 = ttk.Button(root, text='Cancel', command=quit)
button3.grid(row=0, column=2)
button3.place(x=400, y=175)

root.mainloop()