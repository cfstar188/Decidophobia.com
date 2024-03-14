import { atom } from "jotai";

const auth = {isAuthenticated: false, username: 'User'};
export const authAtom = atom(auth);
