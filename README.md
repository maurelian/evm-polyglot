# EVM Polyglot

Translations of standard contracts from Solidity to Vyper. Hopefully more languages in the future. 

Each contract has one test suite, which runs against the compiled bytecode output from each language it's implemented in. 

## Motivations

1. Learn Vyper, and better understand how it differs from Solidity. 
2. Develop a better understanding of [ERC standard contracts](https://eips.ethereum.org/erc) by reimplementing them in Vyper.

## Installation

* `npm i`


## Compiling Contracts

In order to compile the vyper contracts, you will need to have Vyper installed locally, and available in your Path. If you can't compile a vyper contract from the command line, you can't compile using this project. 

Compiler output from vyper contracts is stored using the `Truffle Contract Schema`. This enables vyper contracts to be used in a test suite written for truffle.

To compile all contracts, simply run `npm run compile`. 

It's also possible to compile a single language using:

* `npm run compile:solidity` 
* `npm run compile:vyper` 

Or vyper files in a single directory using `node build_vyper.js /path/to/dir`.

## Running tests

`npm run test`

## How tests are implemented

Tests are written to take advantage of Truffle's testing utilities, so that existing test suites written for solidity implementations can be re-used with minimal modifications.

### Incompatibilities

Where a test is failing due to a known and irreconcilable incompatibility between solidity and vyper, I've caused the test to fail immediately with an explanatory note:

```
if (lang === 'Vyper') {
  assert(false, `Vyper doesn't have a 'fallback' function.`);
}
```
