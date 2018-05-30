module.exports = {
  networks: {
    // optional network config values
    // host - defaults to "localhost"
    // port - defaults to 8545
    // gas
    // gasPrice
    // from - default address to use for any transaction Truffle makes during migrations
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*" // Match any network id
    },
    coverage: {
      host: "localhost",
      network_id: "*",
      port: 8555,        
      gas: 0xfffffffffff,
      gasPrice: 0x01     
    },
  }
}
