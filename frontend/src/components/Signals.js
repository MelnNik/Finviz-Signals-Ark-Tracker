import React, { Component } from 'react';
import axios from 'axios';
import { Alert } from 'react-bootstrap';

class Signals extends Component {
  state = {
    signals: [],
  };

  componentDidMount() {
    axios.get('api/trade-list/?format=json').then((res) => {
      const signals = res.data;
      this.setState({ signals });
    });
  }
  render() {
    return (
      <div>
        {this.state.signals.map((signal) => (
          <div>
            {signal.move ? (
              <Alert variant='success'> {signal.ticker} </Alert>
            ) : (
              <Alert variant='danger'> {signal.ticker} </Alert>
            )}
          </div>
        ))}
      </div>
    );
  }
}

export default Signals;
