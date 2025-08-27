export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const results = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      results.push(value.slice(startString.length));
    }
  }

  return results.join('-');
}
