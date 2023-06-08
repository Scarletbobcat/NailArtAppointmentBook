import { Link } from 'react-router-dom';

const Navbar = () => {
    return ( 
        <nav className="navbar">
            <Link className="home" to="/">Nail Art & Spa LLC.</Link>
            <div className="links">
                <Link to="/create-appointment">Create Appointment</Link>
                <Link to="/delete-appointment">Delete Appointment</Link>
                <Link to="/nail-techs">Nail Techs</Link>
            </div>
        </nav>
     );
}
 
export default Navbar;