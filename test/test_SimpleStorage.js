const { assertRevert } = require('./helpers/assertRevert');

const solidity_SimpleStorage = artifacts.require('solidity_SimpleStorage');
const vyper_SimpleStorage = artifacts.require('vyper_SimpleStorage');

// run tests
test(vyper_SimpleStorage, 'Vyper')
test(solidity_SimpleStorage, 'Solidity')

function test(SimpleStorage, lang) {
  let ss; // init an empty variable that will occupy our contract
  
  contract(`SimpleStorage: ${lang}`, (accounts) => {
    beforeEach(async () => {
      ss = await SimpleStorage.new({ from: accounts[0] });
    });

    it('Initializes with a value of zero', async () => {
      const value = await ss.value();
      assert.equal(value.toNumber(), 0);
    });

    it('calling setValue changes the value', async () => {
      let value = await ss.value();
      assert.equal(value.toNumber(), 0);

      await ss.setValue(10, { from: accounts[0] });
      value = await ss.value();
      assert.equal(value.toNumber(), 10);

      await ss.setValue(457, { from: accounts[0] });
      value = await ss.value();
      assert.equal(value.toNumber(), 457);
    });

    it('Should not accept ether payments to the fallback', async () => {
      if (lang == 'Vyper'){
        assert(false, 'Vyper does not support fallback functions');
      }
      const balanceBefore = await web3.eth.getBalance(ss.address);
      assert.strictEqual(balanceBefore.toNumber(), 0);

      await assertRevert(new Promise((resolve, reject) => {
        web3.eth.sendTransaction({ from: accounts[0], to: ss.address, value: web3.toWei('10', 'Ether') }, (err, res) => {
          if (err) { reject(err); }
          resolve(res);
        });
      }));

      const balanceAfter = await web3.eth.getBalance(ss.address);
      assert.strictEqual(balanceAfter.toNumber(), 0);
    });
  });
}
