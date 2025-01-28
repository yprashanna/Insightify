// Dashboard.test.js - Tests for the Dashboard component

import React from 'react';
import { render } from '@testing-library/react';
import Dashboard from '../Dashboard';

test('renders Dashboard component without crashing', () => {
  render(<Dashboard />);
});