import './global.css';
import { Inter } from 'next/font/google';
import type { ReactNode } from 'react';

import 'katex/dist/katex.css';
import { ThemeProvider } from 'next-themes';
const inter = Inter({
  subsets: ['latin'],
});

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <html lang='en' className={inter.className} suppressHydrationWarning>
      <body className='flex flex-col min-h-screen'>
        {/* <Provider>{children}</Provider> */}
        <ThemeProvider attribute='class' defaultTheme='dark' enableSystem disableTransitionOnChange>
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
