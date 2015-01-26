import palleteImages
import pygame

def setFontSurface(surface):
	font = {
		"0":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"1":palleteImages.paletteImage(surface, [
			[0, 0, 0, 2, 2, 0, 0, 0],
			[0, 0, 2, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 0, 1, 1, 0, 0]
		]),
		"2":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 2, 2, 1, 1, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 2, 2, 1, 1, 0, 0, 0],
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 1, 1, 1, 1, 1, 0],
		]),
		"3":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 2, 2, 1, 1, 0],
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"4":palleteImages.paletteImage(surface, [
			[0, 0, 0, 2, 2, 2, 0, 0],
			[0, 0, 2, 2, 2, 2, 1, 0],
			[0, 2, 2, 1, 2, 2, 1, 0],
			[2, 2, 1, 1, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 2, 1, 0],
			[0, 1, 1, 1, 2, 2, 1, 0],
			[0, 0, 0, 0, 2, 2, 1, 0],
			[0, 0, 0, 0, 0, 1, 1, 0]
		]),
		"5":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[2, 2, 1, 1, 1, 1, 1, 0],
			[2, 2, 0, 0, 0, 0, 0, 0],
			[2, 2, 2, 2, 2, 0, 0, 0],
			[0, 1, 1, 1, 2, 2, 0, 0],
			[2, 2, 0, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"6":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 0, 1, 1, 0],
			[2, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"7":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 1, 1, 2, 2, 1, 0],
			[0, 0, 0, 2, 2, 1, 1, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 2, 2, 1, 1, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 0, 1, 1, 0, 0, 0, 0]
		]),
		"8":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"9":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 2, 1, 0],
			[0, 0, 1, 1, 2, 2, 1, 0],
			[2, 2, 0, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"A":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 2, 1, 0],
			[2, 2, 1, 1, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 0, 0, 1, 1, 0]
		]),
		"B":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 1, 1, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 1, 1, 0],
			[0, 1, 1, 1, 1, 1, 0, 0]
		]),
		"C":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 0, 1, 1, 0],
			[2, 2, 1, 0, 0, 0, 0, 0],
			[2, 2, 1, 0, 0, 0, 0, 0],
			[2, 2, 1, 0, 2, 2, 0, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"D":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 1, 1, 0],
			[0, 1, 1, 1, 1, 1, 0, 0]
		]),
		"E":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 2, 2, 1, 1, 1, 1, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 2, 2, 1, 1, 1, 1, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 0, 1, 1, 1, 1, 1, 0]
		]),
		"F":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 2, 2, 1, 1, 1, 1, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 2, 2, 1, 1, 1, 1, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 0, 1, 1, 0, 0, 0, 0]
		]),
		"G":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 0, 1, 1, 0],
			[2, 2, 1, 0, 0, 0, 0, 0],
			[2, 2, 1, 2, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"H":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 0, 0, 1, 1, 0]
		]),
		"I":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 2, 2, 1, 1, 1, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 1, 1, 1, 1, 1, 0]
		]),
		"J":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 1, 2, 2, 1, 1, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[0, 0, 0, 2, 2, 1, 0, 0],
			[2, 2, 0, 2, 2, 1, 0, 0],
			[0, 2, 2, 2, 1, 1, 0, 0],
			[0, 0, 1, 1, 1, 0, 0, 0]
		]),
		"K":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 2, 2, 1, 1, 0],
			[2, 2, 2, 2, 1, 1, 0, 0],
			[2, 2, 1, 2, 2, 0, 0, 0],
			[2, 2, 1, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 0, 0, 1, 1, 0]
		]),
		"L":palleteImages.paletteImage(surface, [
			[0, 2, 2, 0, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 2, 2, 2, 0, 0],
			[0, 0, 1, 1, 1, 1, 1, 0]
		]),
		"M":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 0, 2, 2, 0],
			[2, 2, 2, 0, 2, 2, 2, 1],
			[2, 2, 2, 2, 2, 2, 2, 1],
			[2, 2, 1, 2, 1, 2, 2, 1],
			[2, 2, 1, 2, 1, 2, 2, 1],
			[2, 2, 1, 2, 1, 2, 2, 1],
			[2, 2, 1, 0, 1, 2, 2, 1],
			[0, 1, 1, 0, 0, 0, 1, 1]
		]),
		"N":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 0, 2, 2, 0],
			[2, 2, 2, 0, 0, 2, 2, 1],
			[2, 2, 2, 2, 0, 2, 2, 1],
			[2, 2, 1, 2, 1, 2, 2, 1],
			[2, 2, 1, 2, 2, 2, 2, 1],
			[2, 2, 1, 0, 2, 2, 2, 1],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[0, 1, 1, 0, 0, 0, 1, 1]
		]),
		"O":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 2, 0, 0],
			[2, 2, 1, 1, 1, 2, 2, 0],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[0, 2, 2, 2, 2, 2, 1, 1],
			[0, 0, 1, 1, 1, 1, 1, 0]
		]),
		"P":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 1, 1, 0],
			[2, 2, 1, 1, 1, 1, 0, 0],
			[2, 2, 1, 0, 0, 0, 0, 0],
			[2, 2, 1, 0, 0, 0, 0, 0],
			[0, 1, 1, 0, 0, 0, 0, 0]
		]),
		"Q":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 2, 2, 2, 0, 0]
		]),
		"R":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 2, 2, 2, 1, 1, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 0, 0, 1, 1, 0]
		]),
		"S":palleteImages.paletteImage(surface, [
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 0, 1, 1, 0],
			[0, 2, 2, 2, 2, 0, 0, 0],
			[0, 0, 1, 1, 2, 2, 0, 0],
			[2, 2, 0, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"T":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[0, 1, 2, 2, 1, 1, 1, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		]),
		"U":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 1, 1, 1, 1, 0, 0]
		]),
		"V":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 1, 0, 2, 1, 1, 0],
			[0, 2, 2, 2, 2, 1, 0, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		]),
		"W":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 0, 2, 2, 0],
			[2, 2, 1, 0, 0, 2, 2, 1],
			[2, 2, 1, 2, 0, 2, 2, 1],
			[2, 2, 1, 2, 1, 2, 2, 1],
			[0, 2, 1, 2, 1, 2, 1, 1],
			[0, 2, 2, 2, 2, 2, 1, 0],
			[0, 0, 2, 1, 2, 1, 1, 0],
			[0, 0, 0, 1, 0, 1, 0, 0]
		]),
		"X":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 2, 2, 2, 2, 0, 0, 0],
			[2, 2, 1, 1, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 1, 1, 0, 0, 1, 1, 0]
		]),
		"Y":palleteImages.paletteImage(surface, [
			[2, 2, 0, 0, 2, 2, 0, 0],
			[2, 2, 1, 0, 2, 2, 1, 0],
			[0, 2, 2, 2, 2, 1, 1, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		]),
		"Z":palleteImages.paletteImage(surface, [
			[2, 2, 2, 2, 2, 2, 0, 0],
			[2, 2, 2, 2, 2, 2, 1, 0],
			[0, 1, 1, 2, 2, 1, 1, 0],
			[0, 0, 2, 2, 1, 1, 0, 0],
			[0, 2, 2, 1, 1, 0, 0, 0],
			[2, 2, 2, 2, 2, 2, 0, 0],
			[2, 2, 2, 2, 2, 2, 1, 0],
			[0, 1, 1, 1, 1, 1, 1, 0]
		]),
		".":palleteImages.paletteImage(surface, [
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 2, 0, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		]),
		"!":palleteImages.paletteImage(surface, [
			[0, 0, 2, 2, 0, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 2, 2, 0, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		]),
		":":palleteImages.paletteImage(surface, [
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 2, 0, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 2, 0, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]
		])
	}
	
	return font
	
def fontPrint(x, y, s, font, scale = 1, pal = 8):
	for char in s:
		if font.has_key(char):
			font[char].draw(x, y, pal, scale)
			x += len(font[char].imageData[0])
		else:
			x += 8

def main():
	screen = pygame.display.set_mode((256, 256))
	newFont = setFontSurface(screen)
	fontPrint(0, 0, "0123456789X", newFont, 1)
	fontPrint(0, 8, "SCORE:", newFont, 1)
	pygame.display.flip()
	running = 1
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0

			
if __name__ == "__main__":
	main()