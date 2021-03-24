import React, { useCallback } from 'react';
import './Menu.css'
import './Dropdown.css'
import TickerInput from './TickerInput'
import DateInput from './DateInput'
import { Button } from 'react-bootstrap'
import { useHistory } from 'react-router-dom';

function Menu() {
    const history = useHistory();
    const handleOnClick = useCallback(() => history.push('/signal'), [history]);


    return (
        <div className="Menu">
            <div className="Menu__reset">
                <Button onClick={handleOnClick} variant="dark">CHECK NEW SIGNALS
                </Button>
            </div>
            <div><TickerInput /></div>
            <div><DateInput /></div>
            <div className="Menu__reset">
                <Button onClick={() => window.location.reload(false)} variant="dark">Reset
                </Button>
            </div>

        </div>
    )
}

export default Menu
