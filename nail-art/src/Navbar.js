const Navbar = () => {
    return ( 
        <nav className="navbar">
            <a className="home" href="/">Nail Art & Spa LLC.</a>
            <div className="links">
                <a href="/create" >Create Appointment</a>
                <a href="/delete">Delete Appointment</a>
                <a href="/techs">Nail Techs</a>
            </div>
        </nav>
     );
}
 
export default Navbar;