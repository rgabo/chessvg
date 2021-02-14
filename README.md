# chessvg

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/rgabo/chessvg)

**chessvg** is an intuitive web application with a fluent API that generates
scalable ([SVG]) images.

## Examples

Every example is also a link that opens in a new tab where you can experiment
with changing the URL.

### Starting position

<a href="https://chessvg.nl" target="_blank">
  <p>https://chessvg.nl</p>
  <img src="https://chessvg.nl" alt="starting position" align="center" width="400" />
</a>

### Position using Forsyth–Edwards Notation (FEN):

The **Giuoco Piano**, a branch of the **Italian Game**, using Forsyth–Edwards Notation:

<a href="https://chessvg.nl/fen/r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R/b" target="_blank">
  <p>https://chessvg.nl/fen/r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R/b</p>
  <img src="https://chessvg.nl/fen/r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R/b" alt="Giuoco Piano" align="center" width="400" />
</a>

### Moves using Standard Algebraic Notation (SAN)

The **Ruy Lopez**, also called the **Spanish Opening** or **Spanish Game**,
using standard algebraic notation:

<a href="https://chessvg.nl/san/e4/e5/Nf3/Nc6/Bc4/Bc5" target="_blank">
  <p>https://chessvg.nl/san/e4/e5/Nf3/Nc6/Bc4/Bc5</p>
  <img src="https://chessvg.nl/san/e4/e5/Nf3/Nc6/Bc4/Bc5" alt="Ruy Lopez" align="center" width="400" />
</a>

### Position from black's perspective

The classical variation of the **King's Indian Defense** from black's perspective using `flip`:

<a href="https://chessvg.nl/san/d4/Nf6/c4/g6/Nc3/Bg7/e4/d6/Nf3/0-0/Be2/e5?flip" target="_blank">
  <p>https://chessvg.nl/san/d4/Nf6/c4/g6/Nc3/Bg7/e4/d6/Nf3/0-0/Be2/e5?flip</p>
  <img src="https://chessvg.nl/san/d4/Nf6/c4/g6/Nc3/Bg7/e4/d6/Nf3/0-0/Be2/e5?flip" alt="King's Indian Defense" align="center" width="400" />
</a>

### Arrows using Portable Game Notation (PGN)

Some ideas of the **King's Indian Attack**, highlighted using arrows:

<a href="https://chessvg.nl/fen/8/8/8/8/8/3P1NP1/PPPNPPBP/R1BQ1RK1?arrows=Re2e4,Re4e5,Bf1e1,Yd2f1,Yh2h4" target="_blank">
  <p>https://chessvg.nl/fen/8/8/8/8/8/3P1NP1/PPPNPPBP/R1BQ1RK1?arrows=Re2e4,Re4e5,Bf1e1,Yd2f1,Yh2h4</p>
  <img src="https://chessvg.nl/fen/8/8/8/8/8/3P1NP1/PPPNPPBP/R1BQ1RK1?arrows=Re2e4,Re4e5,Bf1e1,Yd2f1,Yh2h4" alt="King's Indian Attack" align="center" width="400" />
</a>

## Acknowledgements

**chessvg** would not be possible without Niklas Fiekas' amazing [python-chess]
library. The project also uses the Flask micro-framework,
licensed under Flasks' own [Flask License].

## License

**chessvg** is licensed under GPL 3. See LICENSE for details.

[SVG]: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
[python-chess]: https://github.com/niklasf/python-chess
[Flask License]: https://flask.palletsprojects.com/en/1.1.x/license/