# Solidity-Compatible EIP20/ERC20 Token
# Implements https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
# Author: Phil Daian

# The use of the uint256 datatype as in this token is not
# recommended, as it can pose security risks.

# This token is intended as a proof of concept towards
# language interoperability and not for production use.

# Events issued by the contract
Transfer: event({_from: indexed(address), _to: indexed(address), _value: uint256})
Approval: event({_owner: indexed(address), _spender: indexed(address), _value: uint256})
Truthiness: event({_truthy: bool})

balances: uint256[address]
allowances: (uint256[address])[address]
num_issued: uint256
max_uint_256: public(uint256)

name: public(bytes32)
decimals: public(uint256)
symbol: public(bytes32)


@public
def __init__(_initial_amount: uint256, _token_name: bytes32, _decimals: uint256, _token_symbol: bytes32):
    self.num_issued = _initial_amount
    self.balances[msg.sender] = _initial_amount
    self.name = _token_name
    self.decimals = _decimals
    self.symbol = _token_symbol
    # self.max_uint_256 = 2**256-1 # this line would overflow before subtraction, next is equivalent
    self.max_uint_256 = 2*(2**255-1)+1


@public
@constant
def totalSupply() -> uint256:
    return self.num_issued

@public
@constant
def balanceOf(_owner : address) -> uint256:
    return self.balances[_owner]

@public
def transfer(_to : address, _value : uint256) -> bool:
    _sender: address = msg.sender
    # Make sure sufficient funds are present implicitly through overflow protection
    self.balances[_sender] = self.balances[_sender] - _value
    self.balances[_to] = self.balances[_to] + _value
    # Fire transfer event
    log.Transfer(_sender, _to, _value)
    return True

@public
def transferFrom(_from : address, _to : address, _value : uint256) -> bool:
    _sender: address = msg.sender
    allowance: uint256 = self.allowances[_from][_sender]
    # Make sure sufficient funds/allowance are present implicitly through overflow protection
    self.balances[_from] = self.balances[_from] - _value
    self.balances[_to] = self.balances[_to] + _value
    log.Truthiness(allowance != self.max_uint_256)
    if allowance != self.max_uint_256:
        self.allowances[_from][_sender] = allowance - _value
    # Fire transfer event
    log.Transfer(_from, _to, _value)
    return True

@public
def approve(_spender : address, _value : uint256) -> bool:
    _sender: address = msg.sender
    self.allowances[_sender][_spender] = _value
    # Fire approval event
    log.Approval(_sender, _spender, _value)
    return True

@public
@constant
def allowance(_owner : address, _spender : address) -> uint256:
    return self.allowances[_owner][_spender]
