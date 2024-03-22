import { atomWithStorage } from 'jotai/utils';

const auth = {isAuthenticated: false, username: ''};
export const authAtom = atomWithStorage('auth', { isAuthenticated: false, username: '' });
