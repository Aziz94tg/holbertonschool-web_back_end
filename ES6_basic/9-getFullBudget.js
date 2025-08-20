const fullBudget = {
  ...budget,
  getIncomeInDollars(income) {
    return `$${income}`;
  },
  getIncomeInEuros(income) {
    return `${income} euros`;
  },
};
