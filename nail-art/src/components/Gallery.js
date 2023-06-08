const Gallery = () => {

    const images = ['nails_1.jpeg', 'nails_2.jpeg', 'nails_3.png']

    return (
        <div className="gallery">
            <img src={require(`../images/${images[0]}`)} alt="Nails_1" className="nails_1"/>
            <img src={require(`../images/${images[1]}`)} alt="Nails_2" className="nails_2"/>
            <img src={require(`../images/${images[2]}`)} alt="Nails_3" className="nails_3"/>
        </div>
     );
}
 
export default Gallery;