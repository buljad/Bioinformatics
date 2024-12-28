Задание 5

1. Моей цепочкой было MDKGDVTALPMKKWFTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEAAELEIDKGLVNAVAAVYAEVLARFNDLG
Программами-предсказателями ESMFold и OpenFold, а инструментом выравнивания mulPBA 

2. Использовал ноутбуки https://colab.research.google.com/drive/1bICvUAA6WbRit4mHzuNKTBQeFos2kRKU#scrollTo=HGFBl0QYYQpR и https://colab.research.google.com/drive/15Y92__Veqez6RVIZysCP9ev7SiyvEOlj#scrollTo=XUo6foMQxwS2

3. С их помощью я получил два белка pdb: selected_prediction.pdb и ptm0.602_r3_default.pdb

4. На mulPBA я получил вот такой результат выравнивания:

#Name of files: ptm0 (chain A) and selected_prediction (chain A)
#FASTA of ptm0 chain A and selected_prediction chain A
>ptm0 A
MDKGDVTALPMKKWFTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEAAELEIDKGLVNAVAAVYAEVLARFNDLG
>selected_prediction A
MDKGDVTALPMKKWFTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEAAELEIDKGLVNAVAAVYAEVLARFNDLG
#PBs Assignment
>PB ptm0 A
zzghpagccddddfkboblcacddddfklccddfbfklmmmmmmmmmnopacddddddfklmmmmmpgfklmmgccdfklmmmmmmmmmmmmmmmmmnzz
>PB selected_prediction A
zzddddddddddehjbfbdcddddddfklccddfbfklmmmmmmmmmnopacddddddfklmmmmpccfklpacdddfklmmmmmmmmmmmmmmmmmnzz
#Initial alignment PB
MD--KGDVTALPMKKWFTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEAAELEIDKGLVNAVAAVYAEVLARFNDLG--
--MDKGDVTALPMKKWFTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEAAELEIDKGLVNAVAAVYAEVLARFND--LG
#Final alignment:
--------MDKGDVTALPMKKWF-TT--NYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLAR----TPEA-AELEIDKGLVNAVAAVYAEVLARFNDLG
MDKGDVTA----------LPMKKW-FTTNYHYLVPEVEPSAEIKLNSTKPFDEFNEAKSLGVETKPVFIGPYTFLKLARTPEA--AEL--E-IDKGLVNAVAAVYAEVLARFNDLG
#Scores:
#Alignment score:423.01 RMSD:1.56 Alignment length:116 Number of aligned residues: 84 GDT TS:57.01

а также файлы all_aligned.pdb и визуализацию alignment_ipba.jpg

5. Для визуализации использовал Mol* и сначала визуализировал оба вышеперечисленных белка не выровненными (molstar-visualization-not-aligned.png). Затем визуализировал выровненное pdb соединение (molstar-visualization-aligned.png).
6. Скриншот всего рабочего интерфейса тоже приложен (molstar-screenshot.png)
7. Среди выводов можно выделить:
    Структуры цепей A в ptm0 и selected_prediction показывают высокую степень сходства, особенно с точки зрения последовательностей FASTA.
    Тем не менее, различия в PB указывают на локальные изменения в конформации, что может быть вызвано различными условиями моделирования или тонкими структурными адаптациями.
    Параметры RMSD и GDT TS подтверждают хорошее, но не идеальное соответствие структур. Возможно, дальнейшая оптимизация или анализ могут улучшить выравнивание и соответствие.