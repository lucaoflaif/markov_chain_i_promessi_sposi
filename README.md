# Markov Chain on I Promessi Sposi
This is a Markov chain built from scratch trained on "I promessi sposi" by Alessandro Manzoni.

## Usage
Simply run the `main.py` script with `python main.py`.

## Example
```
➜  markov_i_promessi_sposi python main.py
(N)ew training/(E)xisting model: E
Num of sentences to generate: 5
First word: Le
Le diede al combattimento, ad esterminio de' imbelle. Come sarà facile e. Così dicendo s' aspettavo, tornavano i vantaggi, la maniera da quest' era stata prescritta dalle contese, di gale e come per clientela; e prendere per viottole, che anche il giovine, son morti: ragazzate. Fin da mangiare con un uomo, in mezzo a descriver grand' di Chiuso( Ripam. T' esercito, di stranieri e per lo stomaco, e, non c' aria; e non avendo voluto venire avanti, a piacer mio povero vescovo, come i sei venuto adagio adagio adagio, come morta davvero, se il contatto e fece alcune in Lui.- come cercava d' apertura, certe carrucole; e gli era; ma interrotto da quella voce bassa: ché finalmente speranze, disse il povero tribolato continuamente il castello, e vagabondi.
```

## chain.txt
The `chain.txt` file is a text version of the trained model. There you can see how words are correlated one to each other. All the operations of normalizations, tokenization, weight and probability handling are calculated in runtime. (Check the `utils.py` file to see how they're handled.).

## obj folder
The obj folder contains the pre-trained model loaded using pickle by the script.