//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2018, Image Engine Design Inc. All rights reserved.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//      * Redistributions of source code must retain the above
//        copyright notice, this list of conditions and the following
//        disclaimer.
//
//      * Redistributions in binary form must reproduce the above
//        copyright notice, this list of conditions and the following
//        disclaimer in the documentation and/or other materials provided with
//        the distribution.
//
//      * Neither the name of John Haddon nor the names of
//        any other contributors to this software may be used to endorse or
//        promote products derived from this software without specific prior
//        written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#include "Gaffer/ParallelAlgo.h"

#include "Gaffer/BackgroundTask.h"
#include "Gaffer/Context.h"

#include "boost/make_unique.hpp"

using namespace Gaffer;

void ParallelAlgo::callOnUIThread( const UIThreadFunction &function )
{
	callOnUIThreadSignal()( function );
}

ParallelAlgo::CallOnUIThreadSignal &ParallelAlgo::callOnUIThreadSignal()
{
	static CallOnUIThreadSignal s;
	return s;
}

GAFFER_API std::unique_ptr<BackgroundTask> ParallelAlgo::callOnBackgroundThread( const Plug *subject, BackgroundFunction function )
{
	ContextPtr backgroundContext = new Context( *Context::current() );

	return boost::make_unique<BackgroundTask>(

		subject,

		[backgroundContext, function] ( const IECore::Canceller &canceller ) {

			ContextPtr c = new Context( *backgroundContext, canceller );
			Context::Scope contextScope( c.get() );
			function();

		}

	);
}