import PropTypes from 'prop-types'
import React from 'react'
import {useLocation} from 'react-router-dom'

const Header = ({title,}) => {

    return (
        <header className ='header'>
            <h1> {title}</h1>
        </header>
    )
}

Header.defaultProps ={
    title: 'DBS WORKSPACE'
}

Header.propTypes ={
    title: PropTypes.string.isRequired,
    color: PropTypes.string,
    onClick: PropTypes.func
}

export default Header