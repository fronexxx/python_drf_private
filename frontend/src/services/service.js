import axios from "axios";

const baseUrl = '/api';
const contacts = '/contacts';

const axiosInstance = axios.create({
    baseURL: baseUrl,
    headers: {'Content-Type': 'application/json'}
});

const getAllContacts = async (page) => {
    const {data} = await axiosInstance.get(contacts, {params: {page}});
    return data
}

const createUpdateDeleteContacts = {
    createContact: async (contact) => {
        const {data} = await axiosInstance.post(contacts, contact);
        return data
    }
}

export {
    getAllContacts, createUpdateDeleteContacts
}

