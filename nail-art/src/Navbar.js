const Navbar = () => {
    return ( 
        <nav className="navbar">
            <a className="home" href="/">Nail Art & Spa LLC.</a>
            <div className="links">
                <a href="/create" >Create Appointment</a>
                <a href="/delete">Delete Appointment</a>
                <a href="/add">Add Nail Tech</a>
                <a href="/remove">Remove Nail Tech</a>
            </div>
        </nav>
     );
}
 
export default Navbar;