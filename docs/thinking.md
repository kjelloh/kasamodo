# Tänker på hur jag kan bygga mitt eget 'kasamodo'

* [chimes](../chime/index.md)
* [Top README](../README.md)
* [Top Index](../index.md)

## 20260907

I watched youtube video on a Swedish 'house inside a green house'. I have seen the concept before amd now I wonder if we should consider a kasamodo version of this concept?

* I made [Consider a Kasamodo version of the House-in-a-green-house Swedish Atri House in Sikhall Sweden?](../chime/64d5586f/chime.md)

I am now working on making [init_toolchain.py](../apps/init_toolchain.py) to clone the Eigen C++ library for consumption by the kasamodo_app.

* [Eigen home](https://libeigen.gitlab.io)
  * ``` git clone https://gitlab.com/libeigen/eigen.git ```

I created init_toolchain.py with chatGPT vibe-coding and edits (seems to work ok)

## 20260906

So I want to do a test-shot at making the kasamodo app solve for a stiffness matrix using the C++ Eigen library.

* I want to try a python script that git clones Eigen and populate build environment with headert files and paths
  * It seems I should provide a -I directive to the compiler?
  * And include with ""?
  * The C++ preprocessor seems to search for #include "some_file" in local folder structure and listed include paths? 
  * [GCC search paths](https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html)
  * Eigen seem to propose ```#include <>``` [Eigen - Getting Started](https://libeigen.gitlab.io/eigen/docs-5.0/GettingStarted.html)

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