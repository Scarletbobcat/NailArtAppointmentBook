import nails_1 from '../images/nails_1.jpeg'
import nails_2 from '../images/nails_2.jpeg'
import nails_3 from '../images/nails_3.png'

const Home = () => {
    return ( 
        <div className="home">
            <h1 className="gallery-title">Gallery</h1>
            <div className="gallery">
                <img src={nails_1} alt="Nails_1" className="nails_1"/>
                <img src={nails_2} alt="Nails_2" className="nails_2"/>
                <img src={nails_3} alt="Nails_3" className="nails_3"/>
            </div>
        </div>
    );
}
 
export default Home;