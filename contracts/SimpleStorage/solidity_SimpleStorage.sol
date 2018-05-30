pragma solidity ^0.4.18;

contract solidity_SimpleStorage {

  uint public value;

  function setValue(uint _value) external {
    value = _value;
  }
}