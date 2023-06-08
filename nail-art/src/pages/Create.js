import CreateForm from './CreateForm';

const Create = () => {

    const labels = [{label: "Date", id: 0}, {label: "Name", id: 1}, {label: "Start Time", id: 2}, {label: "End Time", id: 3}, {label: "Phone Number", id: 4}, {label: "Service", id: 5}, {label: "Nail Tech", id: 6}];
    

    return (  
        <div className="create">
            <h1>Create an apppointment</h1><br />
            { labels && <CreateForm data={ labels }></CreateForm> }
        </div>
    );
}
 
export default Create;