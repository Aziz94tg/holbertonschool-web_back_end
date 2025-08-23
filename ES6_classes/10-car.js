export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Ctor = this.constructor[Symbol.species] || this.constructor;
    return new Ctor();
  }

  static get [Symbol.species]() {
    return this;
  }
}
