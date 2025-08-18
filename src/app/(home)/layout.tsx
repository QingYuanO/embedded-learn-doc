import type { ReactNode } from 'react';
import { HomeLayout } from 'fumadocs-ui/layouts/home';
import { baseOptions } from '@/app/layout.config';
import { Provider } from '../provider';
export default function Layout({ children }: { children: ReactNode }) {
  return (
    <Provider>
      <HomeLayout {...baseOptions}>{children}</HomeLayout>
    </Provider>
  );
}
