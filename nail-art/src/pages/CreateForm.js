const CreateForm = ({data, button}) => {

    return (  
        <div className="form1">
            <form className="form" action="/create-appointments">
                { data.map ((labels) => (
                    <div>
                        <label htmlFor={`${labels.label}`} key={ labels.id }>{ labels.label }: </label>
                        <input id={`${labels.label}`} name={`${labels.label}`} type="text" key={ labels.id + 6}/><br /><br />
                    </div>
                ))}
                <input type="submit" value={ button } />
            </form>
        </div>
    );
}
 
export default CreateForm;