function printNumber(n) {
    return n.toLocaleString();
}
function printCurrency(n) {
    return n.toLocaleString('en-US', { style: 'currency', currency: 'USD' })
}


export const HOLDING_COLUMNS = [
    {
        Header: 'Date',
        Footer: 'Date',
        accessor: 'date',
        sticky: 'left'
    },
    {
        Header: 'Ticker',
        Footer: 'Ticker',
        accessor: 'ticker',
        sticky: 'left'
    },
    {
        Header: 'Fund',
        Footer: 'Fund',
        accessor: 'fund',
        sticky: 'left'
    },
    {
        Header: 'Company',
        Footer: 'Company',
        accessor: 'company',
        sticky: 'left'
    },

    {
        Header: 'Holding',
        Footer: 'Holding',
        accessor: 'holding',
        Cell: props => <>{printNumber(props.value)}</>
    },
    {
        Header: 'Market Value',
        Footer: 'Market Value',
        accessor: 'market value($)',
        Cell: props => <>{printCurrency(props.value)}</>
    },
    {
        Header: 'Weight',
        Footer: 'Weight',
        accessor: 'weight(%)',
        Cell: props => <>{printNumber(props.value)}%</>
    }
]