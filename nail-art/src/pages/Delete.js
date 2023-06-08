import CreateForm from './CreateForm'

const Delete = () => {

    const labels = [{label: "Date", id: 0}, {label: "Name", id: 1}, {label: "Start Time", id: 2}]

    return (  
        <div className="delete">
            <h1>Delete Appointment</h1><br />
            <CreateForm data={ labels }></CreateForm>
        </div>
    );
}
 
export default Delete;