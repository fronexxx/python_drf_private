import {useEffect, useState} from "react";
import {useSearchParams} from "react-router-dom";
import {getAllContacts} from "../services/service";
import {ContactComponent} from "./ContactComponent";
import ContactForm from "./ContactForm";
import './ContactsComponent.css';

const ContactsComponent = () => {
    const [contacts, setContacts] = useState([]);
    const [pageInfo, setPageInfo] = useState({})
    const [searchParams, setSearchParams] = useSearchParams();
    const page = Number(searchParams.get('page')) || 1

    const loadContacts = () => {
        getAllContacts(page).then(value => {
            setContacts(value.data);
            setPageInfo({prev: value.prev, next: value.next})
        });
    }
    useEffect(() => {
        loadContacts()
    }, [page]);
    return (
        <div className="contacts">
            <ContactForm onCreated={loadContacts}/>

            <div className="contacts-list">
                {contacts.map(contact => <ContactComponent key={contact.id} contact={contact}/>)}
            </div>

            <div className="pagination">
                <button disabled={!pageInfo.prev} onClick={() => setSearchParams({page: page - 1})}>prev</button>
                <button disabled={!pageInfo.next} onClick={() => setSearchParams({page: page + 1})}>next</button>
            </div>
        </div>
    );
};

export {
    ContactsComponent
}

