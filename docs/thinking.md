# Tänker på hur jag kan bygga mitt eget 'kasamodo'

* [chimes](../chime/index.md)
* [Top README](../README.md)
* [Top Index](../index.md)

## 20260926

Time to introduce conan package manager for kasamodo app.

* It seems my 'bang' git repo has some clues on how to initiate a conan consumer?
* I searched for where I have documented 'conan new ...'

```sh
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub % grep -Fn 'conan new cmake_exe' **/*.md
advent_of_code_2025/docs/README.md:54:Scaffholding has been created with 'conan new cmake_exe ...'
advent_of_code_2025/docs/README.md:57:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/advent_of_code_2025 % conan new cmake_exe -d name=aoc25 -d version=1.0
bang/docs/README.md:67:* Conan package manager support and directory structure (from 'conan new cmake_exe ...' template)
cadance/README.md:16:### conan new cmake_exe -d name=cadance -d version=0.0
cadance/README.md:21:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/cadance % conan new cmake_exe -d name=cadance -d version=0.0
cpp_gfx_tapas/tapas_0/doc/README.md:21:##  conan new cmake_exe -d name=tapas_0 -d version=0.0
cpptha/docs/README.md:114:## conan new cmake_exe -d name=cpptha -d version=0.0
cpptha/docs/README.md:119:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/cpptha % conan new cmake_exe -d name=cpptha -d version=0.0
kasamodo/chime/99447132/chime.md:10:  * It seems to rely on 'conan new cmake_exe ...' template?
kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub % 
```

* advent_of_code_2025/docs/README.md:54:Scaffholding has been created with 'conan new cmake_exe ...'
  * advent_of_code_2025/docs/README.md:57:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/advent_of_code_2025 % conan new cmake_exe -d name=aoc25 -d version=1.0
* bang/docs/README.md:67:* Conan package manager support and directory structure (from 'conan new cmake_exe ...' template)
* cadance/README.md:16:### conan new cmake_exe -d name=cadance -d version=0.0
  * cadance/README.md:21:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/cadance % conan new cmake_exe -d name=cadance -d version=0.0
* cpp_gfx_tapas/tapas_0/doc/README.md:21:##  conan new cmake_exe -d name=tapas_0 -d version=0.0
* cpptha/docs/README.md:114:## conan new cmake_exe -d name=cpptha -d version=0.0
  * cpptha/docs/README.md:119:kjell-olovhogdahl@MacBook-Pro ~/Documents/GitHub/cpptha % conan new cmake_exe -d name=cpptha -d version=0.0
* kasamodo/chime/99447132/chime.md:10:  * It seems to rely on 'conan new cmake_exe ...' template?
  * [Consider a git clone/pull external source dependancies mechanism as a python script?](../chime/99447132/chime.md)

OK. So The command 'conan new cmake_exe -d name=kasamodo_app -d version=0.0' it is!

* [Conan 2.0: conan new](https://docs.conan.io/2/reference/commands/new.html)

## 20260907

I watched youtube video on a Swedish 'house inside a green house'. I have seen the concept before amd now I wonder if we should consider a kasamodo version of this concept?

* I made [Consider a Kasamodo version of the House-in-a-green-house Swedish Atri House in Sikhall Sweden?](../chime/64d5586f/chime.md)

I continued to work on [Consider a git clone/pull external source dependancies mechanism as a python script?](../chime/99447132/chime.md)

## 20260906

So I want to do a test-shot at making the kasamodo app solve for a stiffness matrix using the C++ Eigen library.

* See [Consider a git clone/pull external source dependancies mechanism as a python script?](../chime/99447132/chime.md)

## 20260903

So I have discovered I actually have two kasamodo git respos.

* I created the original one the summer of 2025 on Github
* Then I created a second one local on my laptop with external harddrive backup.

To I decided to merge what I have locally to the Github hosted kasamodo repo.

* First I need to clean up and commit the C++ console app stuf I have initiated so far.
* Then I need a way to bit-by-bit move what I have in the local repo to the Github hosted repo and commit it there.

I don't think it is worth it to figure out a git-way of merging commits made to two git repos?

## 20260823

Kanske är det dags att reda ut hur jag räknar på belastningen på en hus-stomme på fyra ben (plintar)?

* Vilken matte var det igen som man använder?
  * Det har något att göra med en skjuv-modul om jag kommer ihåg rätt?
* Kan jag hacka ihop en finita-elementa funktion för att räkna på en trä-vägg med fackverk?

Jag tänker på det i [Överväg metoder för att kunna beräkna belastning och deformation på hus-stomme på fyra hörn-plintar?](../chime/ec0c2f75/chime.md).

## 20260822

Såg en youtube video om 'counterflow interaction' och skrev ner [Consider to use off-the-shelf available counter flow heat exchanger for Kasamodo ventilation heat-exchange?](../chime/ceaba322/chime.md)


## 20260310

Youtube serverade mig en video som påminde mig om att förse fönstren med natt-luckor för värmeisolering.

* Fönster
  - krage av limträ
  - Fönster längst ut mot fasad
  - Möjligen egen ram med vanliga fönsterglas
  - Möjligen det tredje glaset mot innerväggen
  - Natt-luckor på insidan?
  - Natt-luckor som 'rullgardin' inne i krage?
  - Jag misstänker att Natt-luckor på insidan kan skapa kondens på innerglas?
* Stomme
  - Fyra ben

## 20260304

Så har jag skapat ett 'hem' där jag kan tänka på mitt eget hus som också blir ett frö till det publika 'kasamodo'.

Här kan jag spara mina Freecad-filer, beräkningar, svenska reglöer för bygglov och så vidare. Alltså allt jag behöver red ut för att kunna ha ett hus att bygga samt förstå hur jag kan få bygglov för att bygga det.