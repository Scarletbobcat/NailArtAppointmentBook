import CreateForm from './CreateForm';

const NailTechs = () => {

    const labels = [{label: "Name: ", id: 0}]

    return (  
        <div className="nail-techs">
            <h1>Nail Techs</h1>
            { labels && <CreateForm data={ labels } button="Add"></CreateForm> }
            <input type="submit" value="Delete" />
        </div>
    );
}
 
export default NailTechs;