import os
from shutil import copyfile
	
def MISSION_KST(mis, txt):
#------------------------------------------------------------------------------------------------------
	def readint(x):
		x = kst.read(x)
		x = int.from_bytes(x, byteorder='little')
		return x
#------------------------------------------------------------------------------------------------------
	def writeint(x, y):
		kst.write(x.to_bytes(y, byteorder='little', signed=True))
		return x
#------------------------------------------------------------------------------------------------------
	def readString(f):
		chars = []
		while True:
			c = f.read(1).decode('utf-8')
			if c == chr(0):
				return "".join(chars)
			chars.append(c)
#------------------------------------------------------------------------------------------------------
	def readtext(f):
		text = []
		while True :
			c = f.readline()
			if c[5:10] == "-----":
				return "".join(text)
			text.append(c)
#------------------------------------------------------------------------------------------------------
	poi =(0,1,2,
3,1,4,
5,6,7,
8,1,9,
10,1,11,
12,1,13,
14,1,15,
16,1,17,
18,1,19,
20,1,21,
22,1,23,
24,1,25,
26,1,27,
28,29,30,
31,1,32,
33,1,34,
35,36,37,
38,39,40,
41,42,43,
44,1,45,
46,1,47,
48,1,49,
50,36,51,
52,1,53,
54,29,55,
56,1,57,
58,1,59,
60,1,61,
62,1,63,
64,1,65,
66,36,67,
68,1,69,
70,1,71,
72,73,74,
75,29,76,
77,1,78,
79,1,80,
81,1,82,
83,1,84,
85,1,86,
87,36,88,
89,1,90,
91,1,92,
93,1,94,
95,1,96,
97,36,98,
99,1,100,
101,1,102,
103,1,104,
105,1,106,
107,36,108,
109,1,110,
111,1,112,
113,1,114,
115,1,116,
117,1,118,
119,1,120,
121,1,122,
123,36,124,
125,1,126,
127,1,128,
129,1,130,
131,36,132,
133,36,134,
135,1,136,
137,36,138,
139,36,140,
141,36,142,
143,36,144,
145,1,146,
147,1,148,
149,1,150,
151,152,153,
154,1,155,
156,1,157,
158,1,159,
160,1,161,
162,1,163,
164,36,165,
166,1,167,
168,1,169,
170,171,172,
173,174,175,
176,177,178,
179,180,181,
182,1,183,
184,1,185,
186,1,187,
188,171,189,
190,36,191,
192,36,193,
194,177,195,
196,174,197,
198,174,199,
200,174,201,
0,1,2,
3,1,4,
5,1,202,
8,1,9,
10,1,11,
12,1,13,
14,1,203,
16,1,204,
18,1,19,
20,1,21,
22,1,23,
24,1,205,
26,1,27,
28,1,206,
31,1,32,
33,1,34,
207,1,208,
35,1,209,
41,1,210,
44,1,45,
46,1,47,
48,1,49,
50,1,211,
52,1,53,
54,1,212,
213,1,214,
56,1,57,
58,1,59,
60,1,61,
62,1,63,
64,1,65,
66,1,215,
216,1,217,
68,1,69,
70,1,71,
72,1,218,
75,1,219,
77,1,220,
79,1,80,
221,1,222,
81,1,82,
223,1,224,
83,1,225,
85,1,86,
87,1,226,
89,1,90,
227,1,228,
229,36,230,
91,1,92,
93,1,94,
231,1,232,
95,1,96,
97,1,233,
99,1,100,
101,1,102,
103,1,104,
234,1,235,
236,1,237,
105,1,106,
107,36,238,
239,1,240,
241,1,242,
109,1,110,
111,1,112,
113,1,114,
115,1,116,
117,1,118,
119,1,120,
121,1,122,
123,36,243,
244,1,245,
125,1,126,
246,1,247,
248,1,249,
127,1,128,
250,1,251,
129,1,130,
131,1,252,
135,1,136,
137,1,253,
139,36,140,
254,1,255,
256,1,257,
141,1,258,
259,1,260,
261,1,262,
143,36,144,
263,1,264,
265,1,266,
267,1,268,
145,1,146,
269,36,270,
271,1,272,
273,36,274,
275,1,276,
147,1,148,
277,1,278,
149,1,150,
279,1,280,
281,1,282,
151,1,283,
154,1,155,
284,36,285,
156,1,286,
287,1,288,
289,1,290,
158,1,159,
291,1,292,
293,1,294,
295,1,296,
160,1,161,
297,1,298,
299,1,300,
301,1,302,
162,1,163,
303,1,304,
305,1,306,
307,1,308,
309,1,310,
164,36,311,
312,1,313,
314,1,315,
316,1,317,
318,1,319,
320,1,321,
322,1,323,
324,1,325,
326,1,327,
328,1,329,
330,1,331,
332,1,333,
334,1,335,
336,1,337,
338,1,339,
340,1,341,
342,1,343,
344,1,345,
346,1,347,
348,1,349,
350,1,351,
352,1,353,
354,1,355,
356,1,357,
358,1,359,
360,1,361,
362,1,363,
364,1,365,
366,1,367,
368,1,369,
370,1,371,
372,1,373,
374,1,375,
376,1,377,
378,1,379,
380,1,381,
382,1,383,
384,1,385,
386,1,387,
388,1,389,
390,1,391,
392,1,393,
394,1,395,
396,1,397,
398,1,399,
400,1,401,
402,1,403,
404,1,405,
406,1,407,
408,1,409,
410,1,411,
412,1,413,
414,1,415,
416,1,417,
418,1,419,
420,1,421,
422,1,423,
424,1,425,
426,1,427,
428,1,429,
430,1,431,
432,1,433,
434,1,435,
436,1,437,
438,1,439,
440,1,441,
442,1,443,
444,1,445,
446,1,447,
448,1,449,
450,1,451,
452,1,453,
454,1,455,
456,1,457,
458,1,459,
460,1,461,
462,1,463,
464,1,465,
466,1,467,
468,1,469,
470,1,471,
472,1,473,
474,1,475,
476,1,477,
478,1,479,
480,1,481,
482,1,483,
484,1,485,
486,1,487,
488,1,489,
490,1,491,
492,1,493,
494,1,495,
496,1,497,
498,1,499,
500,1,501,
502,1,503,
504,1,505,
506,1,507,
508,1,509,
510,1,511,
512,1,513,
514,1,515,
516,1,517,
518,1,519,
520,1,521,
522,1,523,
524,1,525,
526,1,527,
528,1,529,
530,1,531,
532,1,533,
534,1,535,
536,1,537,
538,1,539,
540,1,541,
542,1,543,
544,1,545,
546,1,547,
548,1,549,
550,1,551,
552,36,553,
554,1,555,
166,1,556,
168,1,169,
557,1,558,
170,1,559,
173,1,560,
176,1,561,
179,36,562,
182,1,183,
184,1,185,
186,1,187,
188,1,563,
190,1,564,
192,1,565,
194,1,566,
196,36,567,
198,36,568,
200,36,569,
570,1,571,
572,1,573,
574,1,575,
576,1,577,
578,1,579,
580,1,581,
582,1,583,
584,1,585,
586,1,587,
588,1,589,
590,1,591,
592,1,593,
594,1,595,
596,1,597,
598,1,599,
600,1,601,
602,1,603,
604,1,605,
606,1,607,
608,1,609,
610,1,611,
612,1,613,
614,1,615,
616,1,617,
618,1,619,
620,1,621,
622,1,623,
624,1,625,
626,1,627,
628,1,629,
630,1,631,
632,1,633,
570,1,634,
584,1,585,
586,1,587,
588,1,589,
590,1,591,
594,1,595,
596,1,597,
600,1,601,
)
	kst = open (mis, 'r+b')
	f = open(txt, 'r', encoding='utf-8')
	kst.seek(0xc)
	total = readint(4)
	kst.seek(0x10b5a)
	i = 0
	pointer = ()
	pad = b'\x00'
	filename = os.path.basename(f.name)
	src_name = os.path.abspath(kst.name)
	print("convert ",filename)
	nama_msg = f.readline()[5:-1]
	encoding = f.readline()[9:-1]
	CRLF = f.readline()[5:-1]
	ID = f.readline()[3:-1]
	type = f.readline()[5:-1]
	jumlah_string = int(f.readline()[14:-1])
	sam = f.readline()
	sam = f.readline()
	STATUS = f.readline()
	TRANSLATOR = f.readline()
	LAST_CHECK = f.readline()
	sam = f.readline()
	while i <635:
		offset = kst.tell()
		pointer = pointer + (offset,)
		num= f.readline()
		string = readtext(f).encode('utf-8')
		size = len(string)
		writeint(size,2)
		term = size%2+1
		kst.write(string[:-1])
		kst.write(pad*term)
		i+=1
	print("SIP!")
	kst.seek(0x1124)
	z= 0
	k=0
	while z< 394:
		unk1 = kst.read(148)
		writeint(pointer[poi[k]],4)
		k+=1
		writeint(pointer[poi[k]],4)
		k+=1
		writeint(pointer[poi[k]],4)
		k+=1
		z+=1
	copyfile(src_name,src_name[:-16]+ "0053_mission.kst")
	copyfile(src_name,src_name[:-16]+ "0096_mission.kst")
	copyfile(src_name,src_name[:-16] +"4526_mission.kst")
	kst.close()
	f.close()
	